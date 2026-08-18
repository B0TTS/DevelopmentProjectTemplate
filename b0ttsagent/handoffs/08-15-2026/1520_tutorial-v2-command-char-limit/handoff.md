# Handoff: Implement tutorial-v2 command character limit

## Source

Full decision trail (verbatim transcript, 17 entries, closed): `b0ttsagent/handoffs/08-15-2026/1520_tutorial-v2-command-char-limit/grill-session-tutorial-v2-command-char-limit.json`. This doc carries the actionable summary; the JSON holds the raw Q&A and self-resolved decisions.

## What was accomplished

A grill-me-v3 session (paired with karpathy-guidelines and write-a-skill-v2 conventions) reached shared understanding on improving the `tutorial-v2` skill's command handling. Nothing has been implemented yet — the grilling is complete, the edits are not started.

## Decided design

- **100-character command limit**: commands under 100 chars display inline; at/over 100 chars get written to a file, never shown for copy-paste (user's Windows shell mangles pasted commands).
- **Location**: `b0ttsagent/tutorial/<tutorial-slug>/` — created when a tutorial starts (Phase 1) — with three subfolders:
  - `commands/` — command lines the user runs (one logical command, even if multi-line or over the limit)
  - `scripts/` — standalone agent-authored scripts the user runs or deploys (e.g., to the VPS); multiple commands/loops/functions = script
  - `misc/` — anything not runnable (config, notes, saved output)
- **Shells**: PowerShell is the default unless the tutorial explicitly states otherwise; VPS work runs bash over ssh.
- **Runner mechanics**: the agent always provides a short runner, itself under 100 chars — a short `cd` into the folder plus a relative execute: `.\stepN.ps1` locally, `ssh <host> "bash -s" < stepN.sh` remotely.
- **Scope of the rule**: limit counts full command text; applies everywhere commands are displayed (Phase 1 plan — over-limit commands described, not shown — and Phase 2 steps).
- **Skill edit shape**: one new bullet in the Rules section + a one-line hook in Phase 2's "present the step" item. Surgical — no other changes.
- **Retire v1**: move `.agents/skills/tutorial/` → `b0ttsagent/depricated/skills/tutorial/` (established retirement area; `grill-me-v2`, `write-a-skill` already live there). Out of the skills load path, so no `disable-model-invocation` needed. tutorial-v2 becomes the only live tutorial skill.

## Open decisions

None — decision tree exhausted.

## Suggested skills for the next session

- `write-a-skill-v2` — governs the SKILL.md edit (surgical, description/checklist rules)
- `karpathy-guidelines` — surgical changes only, no speculative flexibility
- `markdown-doc-designs` — optional readability pass on the edited SKILL.md

## Key files

- Skill to edit: `.agents/skills/tutorial-v2/SKILL.md`
- Skill to retire: `.agents/skills/tutorial/SKILL.md` (move whole folder)
- Retirement target: `b0ttsagent/depricated/skills/`
- New runtime location (created by tutorials at Phase 1, not now): `b0ttsagent/tutorial/<slug>/{commands,scripts,misc}/`
- Session log: `b0ttsagent/handoffs/08-15-2026/1520_tutorial-v2-command-char-limit/grill-session-tutorial-v2-command-char-limit.json`
