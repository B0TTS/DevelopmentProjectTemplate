# Handoff: Daily Streak Tracker Research (ClickUp + PC/iOS)

**Date:** 07-19-2026
**Status:** Research complete; decision pending ONE user answer
**Next action needed:** User decides PWA-vs-native-iOS tolerance, then agent synthesizes final pick

---

## What was accomplished

Research session into daily streak/habit trackers. User wants, in priority order:
1. **PC (Windows) ↔ iOS sync** — the "above all" requirement
2. **Accessible inside ClickUp** if possible
3. Tracks **both work and personal** habits
4. **Free only** (no subscription; one-time payment reluctantly tolerable)
5. **Clean / minimalistic UI**, gamification irrelevant
6. New pivot: **open source, self-hostable backend, and/or data export** (data ownership)

Three waves of web research were run. No files were created or edited in the repo — this is pure research output.

## Findings (condensed)

### ClickUp native streak tracker: does not exist
- No ClickApp, no built-in streak feature. Open feature requests on ClickUp's feedback board, unfulfilled.
- Only "native" path is DIY: recurring daily tasks + custom fields + Dashboard with an Embed view.
- The only real ClickUp↔habit-app integration is **Habitify via Zapier** (one-way logging). Habitify's free tier = 3 habits, so it fails the "free only" rule.

### Cross-platform (Windows + iOS) landscape
- **Streaks** (Apple Design Award winner) — best streak UX but **Apple-only: no web, no Windows, no Android.** Eliminated by the Windows requirement.
- **Habitica** — free, web + iOS, but busy RPG UI conflicts with "clean/minimal." Demoted. No official Zapier integration (needs viaSocket/Appy Pie).
- **HabitBull** — cloud sync but not real-time; bug/support complaints. Risky.
- **Habit Pocket** — free forever, web-first (Windows via browser), native iOS app, **real-time** sync, minimalist grid UI, no gamification. Free tier caps at **5 habits**, charts 30 days. Pro is a one-time payment (not subscription).
- **Habitify** — best cross-platform polish + the only ClickUp Zapier link, but free tier caps at **3 habits**. Loses on "free only."

### Open source / self-hostable
- **Beaver Habits** — Python, Docker, BSD-3, ~1.8k★. Clean, minimal, streak-only ("no goals" philosophy). **PWA only on iOS** (no native app). Best minimalism + self-host fit.
- **OpenHabitTracker** — C# Blazor, Docker, GPL-3. **Native iOS** + web + Windows. Export in **Markdown/YAML/JSON/TSV**. Most complete feature set; weak spot is utilitarian UI.
- **Trakit** — SvelteKit + SQLite, Docker, MIT. Material 3, GitHub-style calendar. Single SQLite file = trivially portable. PWA on iOS.
- **Haby** — single container, homelab-friendly, multi-user. PWA.
- **Habo** — Flutter, **native iOS+Android**, E2E-encrypted sync, self-hostable backend, zero-knowledge. Dark horse; small/unproven (sync reliability unverified).
- **Habitica self-host** — "near-impossible" per community. Skip.

### Data export (without self-hosting)
- **Habit Pocket** — one-click CSV export from settings; JSON export on roadmap; account deletion wipes data in one transaction.
- **Habitify** — CSV + full `.sqlite` backup; can import from Streaks/Productive (but free tier ruled out).
- **Cron Habits** — API-first, full JSON export. Web-focused.

## Current state & the ONE open decision

Research converged on a **triangle tradeoff**: Native iOS app / Self-hosted backend / Clean minimal UI — almost nothing hits all three. Self-hosted options generally give you a PWA on iOS (Safari → add to home screen), not a native App Store app.

**The decision hinges on one question the user has not yet answered:**

> **Is a PWA on the iPhone home screen acceptable, or do you need a native iOS app?**

That answer routes to a final pick:

- **PWA acceptable →** self-host **Beaver Habits** (Docker). Cleanest minimal streak-focused UI, full backend ownership. Windows via browser, iOS via Safari home-screen PWA.
- **Native iOS required, want data ownership →** **Habit Pocket** (free, native iOS + Windows web, real-time sync, one-click CSV export). Owns data in practice without running a server.
- **Native iOS + open source + self-host + export, tolerate utilitarian UI →** **OpenHabitTracker** (checks every box except UI polish).

## Saved questions (from grill-me skill, to ask before final synthesis)

The user capped pre-research grilling at 3 questions. These were held for the post-research synthesis phase and have NOT been answered:

1. How many distinct habits/streaks? (≤5 fits Habit Pocket free; 10+ forces OpenHabitTracker or self-host.)
2. Streak forgiveness rules — strict "don't break the chain" vs skip-days/pause/recovery?
3. Reminder/notification importance?
4. For the work side: is "complete a ClickUp task today" enough, or per-task-type streaks needed?
5. Does the user actually want to run a Docker container / maintain a self-hosted backend, or was "self-host" really just a proxy for "I don't want to be locked in"?

## Suggested skills for next session

- **grill-me** (`skills/grill-me/SKILL.md`) — only if the user wants to resume interrogation; they explicitly capped it last time.
- **creative-brainstorm** (`skills/creative-brainstorm/SKILL.md`) — if the user decides none of the market options fit and wants to brainstorm building a minimal self-hosted streak tracker from scratch.
- **create-nav-guide** (`skills/create-nav-guide/SKILL.md`) — once a tool is chosen and set up, document the setup as a nav guide under `b0ttsagent/NavGuides/`.

## Key paths & references

- This handoff: `b0ttsagent/LookIntoDuringThinkingTime/daily-streak-tracker-clickup-research.md`
- NavGuides live in: `b0ttsagent/NavGuides/` (scan YAML front matter for existing ClickUp/Docker guides that may inform setup)
- No repo files were touched in this session.

## External links worth revisiting (not yet fetched in depth)

- Beaver Habits: https://github.com/daya0576/beaverhabits
- OpenHabitTracker: https://openhabittracker.net/ / https://github.com/jinjinov/openhabittracker
- Trakit: https://gettrakit.app / https://github.com/tylxr59/Trakit
- Habo: https://github.com/xpavle00/Habo
- Habit Pocket: https://habitpocket.io/
- Habitify pricing (3-habit free cap): https://habitify.me/pricing
- Habitify↔ClickUp Zapier: https://zapier.com/apps/clickup/integrations/habitify
- ClickUp Embed view docs: https://help.clickup.com/hc/en-us/articles/6310077597335-Add-an-Embed-view

## Residual risks / things to verify before committing

- **Habit Pocket iframe embedding in ClickUp:** untested. Some web apps block iframe embedding via `X-Frame-Options`/CSP. Quick to verify if user picks the Habit Pocket + ClickUp embed path.
- **Habo sync reliability:** unverified from sources — small project.
- **Self-hosted PWA iOS reliability:** Safari PWA background sync/notifications are weaker than a native app; worth setting expectations if user goes self-host route.
