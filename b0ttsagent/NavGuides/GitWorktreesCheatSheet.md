---
name: GitWorktreesCheatSheet
topics: [git, worktrees, parallel-agents, branches, workflow]
description: "Personal cheat sheet for git worktrees — creating, managing, and cleaning up multiple working directories for parallel agent workflows"
---

# Git Worktrees Cheat Sheet

## What a Worktree Is

One repo, multiple working directories. Each worktree has its own files + its own checked-out branch, but they all share the same `.git` object store and history.

| | Main worktree | Linked worktree |
|---|---|---|
| Location | Your normal repo folder | Anywhere (usually a sibling folder) |
| `.git` | Real directory | Plain file pointing back to main repo |
| Branch | Any branch not used elsewhere | Any branch not used elsewhere |

> A branch can only be checked out in **one** worktree at a time. Trying to check out a branch that's in use elsewhere errors out.

## Core Commands

```bash
# Create a worktree with a NEW branch
git worktree add -b my-feature ../repo-feature

# Create a worktree from an EXISTING branch
git worktree add ../repo-bugfix existing-branch

# Create from a specific commit (detached HEAD)
git worktree add --detach ../repo-test abc1234

# List all worktrees
git worktree list
```

Convention: put worktrees as **siblings** of the main repo (`../repo-<name>`), not inside it.

## Cleanup

```bash
# Remove a clean worktree (run from anywhere)
git worktree remove ../repo-feature

# Remove one with uncommitted changes (destroys them)
git worktree remove --force ../repo-feature

# Deleted the folder manually? Clean up git's records:
git worktree prune
```

Removing the worktree does **not** delete its branch — do that separately:

```bash
git branch -d my-feature    # safe delete (merged only)
git branch -D my-feature    # force delete
```

## Parallel Agent Workflow

```bash
# 1. Give each agent its own worktree + branch
git worktree add -b agent/task-a ../repo-agent-a
git worktree add -b agent/task-b ../repo-agent-b

# 2. Agents work in their own folders — zero interference

# 3. Review their work from the main repo
git diff main..agent/task-a

# 4. Merge back
git merge agent/task-a

# 5. Clean up
git worktree remove ../repo-agent-a
git branch -d agent/task-a
```

## Gotchas

> **Ignored files aren't shared.** Each worktree gets a fresh working directory — `node_modules`, `.env`, build output, etc. must be installed/copied per worktree.

> **Never manually delete a worktree folder** without running `git worktree prune` after — git keeps stale records otherwise.

> **The main worktree can't be removed or moved.** Only linked ones.

> **Uncommitted changes die with `--force`.** Commit or stash in the worktree first if the work matters.

> **Git auto-prunes stale worktree metadata after 3 months** of the folder being missing — but manual `prune` is instant.

## Quick Reference

| Task | Command |
|---|---|
| New worktree + new branch | `git worktree add -b <branch> <path>` |
| New worktree, existing branch | `git worktree add <path> <branch>` |
| See all worktrees | `git worktree list` |
| Remove clean worktree | `git worktree remove <path>` |
| Remove dirty worktree | `git worktree remove --force <path>` |
| Fix records after manual delete | `git worktree prune` |
| Move a worktree | `git worktree move <path> <new-path>` |
