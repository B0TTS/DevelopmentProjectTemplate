# Handoff: opencode-submodule-setup

**Date:** 07-28-2026

## Summary

Goal: Make the `.opencode` directory in `DevelopmentProjectTemplate` its own git submodule backed by a separate GitHub repo called `OPENCODE-Agent`.

### What was done so far

- Inspected the project: `.opencode` is already its own git repo but with messy history (committed `node_modules/`, `opencode.json` with secrets, `settings.json`) and its remote incorrectly points to the parent repo `B0TTS/DevelopmentProjectTemplate`
- Audit discovered the `.gitignore` is already well-configured — it covers `node_modules/`, `opencode.json`, `settings.json`, lock files, runtime state, etc. The problem was these files were committed before the gitignore took effect
- Decided to **start fresh** (nuke `.git`, re-init cleanly) rather than rewrite history
- No GitHub repo created yet — user will do this as Step 1

### The plan (4 steps)

1. **Create the GitHub repo** — `B0TTS/OPENCODE-Agent`, completely empty (no README, no .gitignore, no license)
2. **Start fresh locally** — delete `.opencode/.git`, `git init` a clean repo inside `.opencode`. The existing `.gitignore` will auto-exclude secrets and `node_modules/`
3. **First commit + push** — add files, commit, set remote to the new repo, push, verify on GitHub
4. **Wire up as submodule** — in the parent repo, `git submodule add https://github.com/B0TTS/OPENCODE-Agent.git .opencode`, commit, push

### Current state

- GitHub repo: **not yet created**
- All steps still pending
- Parent repo has existing submodule `.pi` → `B0TTS/PI-Agent.git` as a reference pattern in `.gitmodules`

## Suggested skills for next session

- `tutorial` — if the user wants step-by-step guidance through the plan

## Key files

| Path | Role |
|------|------|
| `.opencode/` | Directory to become a submodule |
| `.opencode/.gitignore` | Already correct — excludes secrets, node_modules, runtime state |
| `.gitmodules` | Parent's submodule config (already has `.pi` entry) |
| `b0ttsagent/handoffs/07-28-2026/opencode-submodule-setup.md` | This handoff |

## Key commands

```bash
# Step 2: Clean-reinit inside .opencode
cd .opencode
rm -rf .git
git init
git add .
git commit -m "Initial commit: OPENCODE-Agent config"

# Step 3: Connect and push
git remote add origin https://github.com/B0TTS/OPENCODE-Agent.git
git branch -M main
git push -u origin main

# Step 4: Register as submodule (run from parent repo root)
git submodule add https://github.com/B0TTS/OPENCODE-Agent.git .opencode
git add .gitmodules .opencode
git commit -m "Add .opencode as submodule"
```

## Open decisions

- None — plan is fully defined and agreed
