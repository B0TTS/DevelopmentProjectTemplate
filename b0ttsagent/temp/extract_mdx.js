const https = require('https');
const fs = require('fs');

function fetch(url, ua) {
  return new Promise((resolve, reject) => {
    https.get(url, { headers: { 'User-Agent': ua } }, (res) => {
      if (res.statusCode >= 300 && res.statusCode < 400 && res.headers.location) {
        const loc = res.headers.location;
        const next = loc.startsWith('http') ? loc : new URL(loc, url).href;
        return resolve(fetch(next, ua));
      }
      let body = '';
      res.setEncoding('utf8');
      res.on('data', (d) => (body += d));
      res.on('end', () => resolve(body));
    }).on('error', reject);
  });
}

(async () => {
  const ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)';
  const raw = await fetch('https://create.roblox.com/docs/production/promotion/discovery', ua);
  fs.writeFileSync(__dirname + '/roblox_disc.html', raw);
  const m = raw.match(/<script id="__NEXT_DATA__"[^>]*>([\s\S]*?)<\/script>/);
  if (!m) { console.log('no NEXT_DATA'); return; }
  const nd = JSON.parse(m[1]);
  const content = nd.props.pageProps.data.content;

  const out = [];
  let i = 0;
  while (i < content.length) {
    const ch = content[i];
    if (ch === '"' || ch === "'") {
      const q = ch;
      let j = i + 1;
      let buf = '';
      while (j < content.length) {
        const c = content[j];
        if (c === '\\') { buf += content[j + 1] || ''; j += 2; continue; }
        if (c === q) break;
        buf += c;
        j++;
      }
      if (/\s/.test(buf) && /[a-zA-Z]/.test(buf) && buf.length >= 2 && !/^[\s-]+$/.test(buf)) {
        out.push(buf);
      }
      i = j + 1;
    } else { i++; }
  }

  const prose = out.filter(s => !/^(https?:|\.\/)/.test(s) && !(s.length < 4 && /^[a-z][a-zA-Z]*$/.test(s)));
  let text = prose.join('\n');
  text = text.replace(/\n{3,}/g, '\n\n');
  fs.writeFileSync(__dirname + '/roblox_disc_text.txt', text);
  console.log('wrote', text.length, 'chars\n');
  console.log('==================== ROBLOX DISCOVERY DOC (live) ====================\n');
  console.log(text);
})().catch(e => { console.error(e); process.exit(1); });
