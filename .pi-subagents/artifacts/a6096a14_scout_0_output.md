# Code Context

## Files Retrieved
1. Top-level `ls` of `C:\Users\intel\DevelopmentProjectTemplate` — the recon target itself.
2. `find` of top-level (limit 100) — revealed structure under `.agents/` and `b0ttsagent/`.

## Key Findings
Top-level directory contains:

- **Docs**: `README.md` (user-facing setup), `AGENTS.md` (agent instructions), `DESIGN.md`, `GAME-CONTEXT.md`
- **`b0ttsagent/`** — the content hub: handoffs (dated folders), `planningarchives/`, `reports/`, `temp/` (dumping ground)
- **`.agents/skills/`** — skills: `grill-me`, `grill-me-v3` (+scripts), `handoff`, `mermaid-diagrams`, `next-decision`
- **Tooling/config**: `.git/`, `.gitmodules` (submodules for `.opencode` and `.pi`), `.gitignore`, `.opencode/`, `.pi/`, `.pi-subagents/`, `Setup/`
- **Oddity**: a stray `nul` file at top level (Windows artifact) — harmless but noise.

## Start Here
`AGENTS.md` — it defines the execution model (skill-first) and where everything lives; `README.md` is explicitly user-setup-only.