// Usage: node extract_doc.js <htmlfile> [label]
// Extracts Roblox discovery doc prose from a (live or Wayback) SSR HTML file.
const fs = require('fs');
const file = process.argv[2];
const label = process.argv[3] || file;
const raw = fs.readFileSync(file, 'utf8');

let m = raw.match(/<script id="__NEXT_DATA__"[^>]*>([\s\S]*?)<\/script>/);
let content = null;
if (m) {
  try {
    const nd = JSON.parse(m[1]);
    content = nd.props && nd.props.pageProps && nd.props.pageProps.data && nd.props.pageProps.data.content;
  } catch (e) {}
}

const TAGS = new Set(['p','h2','h3','h4','h5','li','br','img','table','tbody','thead','tr','td','th','strong','em','u','a','ol','ul','center','span','div','AccordionDetails','AccordionSummary','BaseAccordion','Typography','code','pre','blockquote','hr','figure','figcaption','video','source','path','svg','g','defs','rect','circle','polyline','line','xmlns','width','height','viewBox','fill','stroke','children','id','href','src','alt','variant','className','style','colspan','rowspan','target','rel','color','d','cx','cy','r','x','y','x1','y1','x2','y2','points','transform','key','ref','dangerouslySetInnerHTML','default','enumerable','value','get','configurable','writable','length','prototype','constructor','call','apply','bind','assign','create','defineProperty','getOwnPropertyDescriptor','getOwnPropertyNames','getPrototypeOf','hasOwnProperty','isExtensible','preventExtensions','exports','module','require','__esModule','default','this','window','document','undefined','function','return','var','let','const','new','throw','typeof','instanceof','void','delete','try','catch','finally','if','else','for','while','switch','case','break','continue','do','in','of','class','extends','super','async','await','yield','import','export','from','as','true','false','null','self','globalThis','Object','Array','String','Number','Boolean','Symbol','Map','Set','Promise','JSON','Math','Date','RegExp','Error','TypeError','SyntaxError','RangeError','Reflect','Proxy','WeakMap','WeakSet','Buffer','process','console','setTimeout','setInterval','requestAnimationFrame']);

function extractProse(src) {
  const out = [];
  let i = 0;
  while (i < src.length) {
    const ch = src[i];
    if (ch === '"' || ch === "'") {
      const q = ch;
      let j = i + 1, buf = '';
      while (j < src.length) {
        const c = src[j];
        if (c === '\\') { buf += src[j + 1] || ''; j += 2; continue; }
        if (c === q) break;
        buf += c; j++;
      }
      // keep if it looks like prose: has a letter, not a known tag/identifier, not a url/path, not pure code
      const looksCode = /^[a-zA-Z_$][a-zA-Z0-9_$]*$/.test(buf) && !/\s/.test(buf);
      const looksTag = TAGS.has(buf);
      const isUrl = /^(https?:|\.\/|\/|\.\.\/|data:|blob:|#)/.test(buf);
      const hasLetter = /[a-zA-Z]/.test(buf);
      const isProseWord = hasLetter && buf.length >= 2 && !looksCode && !looksTag && !isUrl && !/^[\s\W]+$/.test(buf);
      if (isProseWord) out.push(buf);
      i = j + 1;
    } else { i++; }
  }
  return out;
}

let prose;
if (content) {
  prose = extractProse(content);
  console.error(`[${label}] extracted from __NEXT_DATA__.content (${content.length} chars) -> ${prose.length} prose strings`);
} else {
  // fallback: strip tags from body
  const body = raw.replace(/<script[\s\S]*?<\/script>/g, ' ').replace(/<style[\s\S]*?<\/style>/g, ' ').replace(/<[^>]*>/g, ' ').replace(/&[a-z]+;/g, ' ');
  const words = body.split(/\s+/).filter(w => /[a-zA-Z]/.test(w) && w.length >= 3);
  prose = words;
  console.error(`[${label}] NO __NEXT_DATA__ -> fallback body words: ${prose.length}`);
}
console.log(prose.join('\n'));
