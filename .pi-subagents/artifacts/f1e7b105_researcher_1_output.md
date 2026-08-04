# Research: Latest stable Node.js LTS as of mid-2025

## Summary
As of mid-2025 (June–July), the latest stable LTS version of Node.js was **v22.17.0** on the **22.x "Jod" Active LTS line** (released June 24, 2025). Node.js 24.x "Krypton" had shipped as "Current" on May 6, 2025 but did **not** become LTS until October 28, 2025, so it was not yet an LTS release in mid-2025.

## Findings
1. **Node 22.x "Jod" was the Active LTS line, latest patch v22.17.0 (2025-06-24)** — official release announcement confirms the date and LTS status; v22.17.0 was the newest LTS-tagged release in the mid-2025 window. [nodejs.org release post](https://nodejs.org/blog/release/v22.17.0)
2. **Node 24.x was Current, not LTS, in mid-2025** — 24.x initially released 2025-05-06; per the official release schedule its Active LTS phase began 2025-10-28 (the v24.11.0 LTS-transition release notes confirm). [nodejs/Release README](https://github.com/nodejs/release/blob/main/README.md) · [v24.11.0 LTS post](https://nodejs.org/en/blog/release/v24.11.0)
3. **Node 20.x was in Maintenance LTS** — the mid-2025 LTS landscape: 20.x (maintenance), 22.x (active), 24.x (current). 22.x maintenance began 2025-10-21 with EOL 2027-04-30. [nodejs.org releases page](https://nodejs.org/en/about/previous-releases) · [nodejs.org EOL](https://nodejs.org/en/about/eol)
4. **Patch progression on 22.x during 2025** — 22.14.0 (2025-02-11) → 22.15.0 (2025-04-23) → 22.16.0 (2025-05-21) → 22.17.0 (2025-06-24), confirming v22.17.0 as the ceiling at mid-2025. [v22 changelog](https://github.com/nodejs/node/blob/master/doc/changelogs/CHANGELOG_V22.md)

## Sources
- Kept: [nodejs.org — v22.17.0 (LTS)](https://nodejs.org/blog/release/v22.17.0) — primary release evidence; [nodejs/Release README](https://github.com/nodejs/release/blob/main/README.md) — authoritative schedule showing 22.x Active LTS / 24.x LTS start date; [Node.js v22 changelog](https://github.com/nodejs/node/blob/master/doc/changelogs/CHANGELOG_V22.md) — patch timeline; [nodejs.org — previous releases](https://nodejs.org/en/about/previous-releases) — LTS lifecycle context.
- Dropped: [LogRocket "Node.js 24 is here"](https://blog.logrocket.com/node-js-24-new/) — secondary commentary, redundant with primary sources; [nodejs.org download/archive pages](https://nodejs.org/en/download/archive/v22.17.0) — mirrors, no added information.

## Gaps
No material gaps. Minor caveat: "mid-2025" was interpreted as June–July 2025; if the intended snapshot was exactly May 2025, the latest LTS would be v22.16.0 (2025-05-21). Also note that from October 2025 onward, 24.x became the Active LTS and 22.x moved to maintenance — the answer is time-anchored to the specified window.