/**
 * Context Tiers — 3-line custom footer with tiered context + cost colours.
 *
 * Layout:
 *   Line 1: /full/path/to/project
 *   Line 2: ↑tokens ↓tokens   62,000/200,000 (31%)
 *   Line 3: model-id (branch)  $0.023  ext-status…
 *
 * Context numbers (line 2): 16 tiers — dim-gray → animated rainbow.
 * Cost number    (line 3): 18 tiers — dim-gray → copper→bronze→
 *   green→silver→teal→blue→purple→ruby→orange→gold→diamond◆→
 *   bright-gold✦→rainbow★.
 *
 * All non-tier text uses uniform ANSI-256 grays in the same colour
 * space as the tier colours so everything sits on one visual plane.
 *
 * Unknown / post-compaction context → `???` (reverse video), no %.
 */

import type { AssistantMessage } from "@earendil-works/pi-ai";
import type { ExtensionAPI } from "@earendil-works/pi-coding-agent";
import { truncateToWidth, visibleWidth } from "@earendil-works/pi-tui";

// ── Number formatting ────────────────────────────────────────────────────────

function fmt(n: number): string {
  return String(Math.floor(n)).replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

// ── ANSI escape helpers ──────────────────────────────────────────────────────

const BOLD      = "\x1b[1m";
const UNDERLINE = "\x1b[4m";
const REVERSE   = "\x1b[7m";
const REV_OFF   = "\x1b[27m";
const RESET     = "\x1b[0m";

function fg(n: number): string { return `\x1b[38;5;${n}m`; }

/** Uniform ANSI-256 gray helpers — same colour-space as the tier colours */
const GRAY = {
  path:     fg(245),  // medium    — project directory
  labels:   fg(245),  // medium    — ↑ ↓ $ symbols
  stats:    fg(247),  // lighter   — input/output/cost numbers
  pct:      fg(245),  // medium    — (31%)
  model:    fg(242),  // dim       — model id, branch, ext statuses
};

// ── Tier definitions (16 tiers, absolute tokens) ─────────────────────────────

interface Tier {
  max: number;
  color: number;
  bold?: boolean;
  underline?: boolean;
  sparkle?: boolean;
  diamond?: boolean;  // always-on ◆ (no flicker)
  rainbow?: boolean;
}

const TIERS: Tier[] = [
  { max: 1_000,        color: 242 },                                    //  1: dim gray
  { max: 3_000,        color: 252 },                                    //  2: white
  { max: 7_000,        color: 249 },                                    //  3: light gray
  { max: 15_000,       color: 108 },                                    //  4: light green
  { max: 30_000,       color: 41 },                                     //  5: green
  { max: 50_000,       color: 43 },                                     //  6: teal
  { max: 75_000,       color: 51 },                                     //  7: cyan
  { max: 100_000,      color: 33 },                                     //  8: blue
  { max: 200_000,      color: 39 },                                     //  9: bright blue
  { max: 500_000,      color: 201 },                                    // 10: magenta
  { max: 1_000_000,    color: 93 },                                     // 11: purple
  { max: 10_000_000,   color: 208 },                                    // 12: orange
  { max: 100_000_000,  color: 202,  bold: true },                       // 13: amber bold
  { max: 500_000_000,  color: 220,  bold: true, underline: true },      // 14: gold b+u
  { max: 999_999_999,  color: 226,  bold: true, underline: true,       // 15: bright gold ✦
    sparkle: true },
  { max: Infinity,     rainbow: true, bold: true },                    // 16: rainbow ★
];

const RAINBOW = [196, 208, 220, 226, 46, 51, 39, 33, 93, 201];

// ── Cost tier definitions (18 tiers, $0 → $1 000 000) ────────────────────────

const COST_TIERS: Tier[] = [
  { max: 0.01,     color: 242 },                                          //  1: dim gray
  { max: 0.05,     color: 248 },                                          //  2: light gray
  { max: 0.10,     color: 252 },                                          //  3: white
  { max: 0.25,     color: 137 },                                          //  4: copper
  { max: 0.50,     color: 179 },                                          //  5: bronze
  { max: 1.00,     color: 143 },                                          //  6: sage green
  { max: 2,        color: 71 },                                           //  7: deep green
  { max: 5,        color: 35 },                                           //  8: bright green
  { max: 10,       color: 247 },                                          //  9: silver
  { max: 25,       color: 43 },                                           // 10: teal
  { max: 50,       color: 39 },                                           // 11: blue
  { max: 100,      color: 134 },                                          // 12: purple
  { max: 500,      color: 196 },                                          // 13: ruby red
  { max: 1_000,    color: 202,  bold: true },                             // 14: deep orange bold
  { max: 10_000,   color: 220,  bold: true, underline: true },            // 15: gold b+u
  { max: 100_000,  color: 255,  bold: true, underline: true,              // 16: diamond white ◆
    diamond: true },
  { max: 999_999,  color: 226,  bold: true, underline: true,              // 17: bright gold ✦
    sparkle: true },
  { max: Infinity, rainbow: true, bold: true },                           // 18: rainbow ★
];

// ── Context tier helpers ─────────────────────────────────────────────────────

function getCtxTier(n: number): Tier {
  for (const t of TIERS) if (n <= t.max) return t;
  return TIERS[TIERS.length - 1]!;
}

function styledCtx(n: number, tier: Tier, frame: number): string {
  return applyTierStyle(fmt(n), tier, frame);
}

// ── Cost tier helpers ────────────────────────────────────────────────────────

function getCostTier(n: number): Tier {
  for (const t of COST_TIERS) if (n <= t.max) return t;
  return COST_TIERS[COST_TIERS.length - 1]!;
}

function styledCost(n: number, tier: Tier, frame: number): string {
  return applyTierStyle(`$${n.toFixed(3)}`, tier, frame);
}

// ── Shared style application ─────────────────────────────────────────────────

function applyTierStyle(text: string, tier: Tier, frame: number): string {
  let color: number;
  let prefix = "";
  let suffix = "";

  if (tier.rainbow) {
    color = RAINBOW[frame % RAINBOW.length]!;
    suffix = " ★";
  } else if (tier.sparkle && Math.random() > 0.5) {
    color = tier.color;
    prefix = "✦ ";
  } else if (tier.diamond) {
    color = tier.color;
    prefix = "◆ ";
  } else {
    color = tier.color;
  }

  let style = fg(color);
  if (tier.bold)      style += BOLD;
  if (tier.underline) style += UNDERLINE;

  return `${style}${prefix}${text}${suffix}${RESET}`;
}

// ── Extension entry ──────────────────────────────────────────────────────────

export default function (pi: ExtensionAPI) {
  pi.on("session_start", (_event, ctx) => {
    let frame = 0;
    let animTimer: ReturnType<typeof setInterval> | null = null;

    ctx.ui.setFooter((tui, _theme, footerData) => {
      if (!animTimer) {
        animTimer = setInterval(() => { frame++; tui.requestRender(); }, 800);
      }

      const unsub = footerData.onBranchChange(() => tui.requestRender());

      return {
        dispose: () => {
          unsub();
          if (animTimer) { clearInterval(animTimer); animTimer = null; }
        },
        invalidate: () => {},

        render(width: number): string[] {
          // ── Line 1: project directory ─────────────────────────────────
          const dirLine = `${GRAY.path}${process.cwd()}${RESET}`;

          // ── Line 2: token stats + context usage ───────────────────────
          let input = 0, output = 0, cost = 0;
          for (const e of ctx.sessionManager.getBranch()) {
            if (e.type === "message" && e.message.role === "assistant") {
              const msg = e.message as AssistantMessage;
              input += msg.usage.input;
              output += msg.usage.output;
              cost += msg.usage.cost.total;
            }
          }

          const statsStr =
            `${GRAY.labels}↑${GRAY.stats}${fmt(input)}` +
            `${GRAY.labels} ↓${GRAY.stats}${fmt(output)}${RESET}`;

          const cu = ctx.getContextUsage();
          let ctxStr = "";

          if (cu) {
            const usedOk = cu.tokens != null;
            const maxOk  = cu.contextWindow > 0;

            const usedStr = usedOk
              ? styledCtx(cu.tokens!, getCtxTier(cu.tokens!), frame)
              : `${REVERSE}???${REV_OFF}`;

            const maxStr = maxOk
              ? styledCtx(cu.contextWindow, getCtxTier(cu.contextWindow), frame)
              : `${REVERSE}???${REV_OFF}`;

            const slash   = usedOk && maxOk ? "/" : " / ";

            // Percentage: only show when both numbers are valid
            const pctStr = (usedOk && maxOk && cu.percent != null)
              ? ` ${GRAY.pct}(${cu.percent.toFixed(2)}%)${RESET}`
              : "";

            ctxStr = `${usedStr}${GRAY.stats}${slash}${maxStr}${pctStr}`;
          }

          const line2parts = [statsStr, ctxStr].filter(Boolean);
          const line2 = line2parts.join("  ");

          // ── Line 3: model + branch + cost + extension statuses ────────
          const branch = footerData.getGitBranch();
          const modelText = `${ctx.model?.id || "no-model"}${branch ? ` (${branch})` : ""}`;

          const costSty = styledCost(cost, getCostTier(cost), frame);
          const costText = `${costSty}`;

          const statuses = footerData.getExtensionStatuses();
          let statusText = "";
          if (statuses.size > 0) {
            statusText = "  " + [...statuses.values()].join("  ");
          }

          const line3 = `${GRAY.model}${modelText}  ${costText}${statusText}${RESET}`;

          // ── Render ────────────────────────────────────────────────────
          return [
            truncateToWidth(dirLine, width),
            truncateToWidth(line2, width),
            truncateToWidth(line3, width),
          ];
        },
      };
    });
  });
}
