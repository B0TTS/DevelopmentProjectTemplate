---
name: youtube-transcript
description: Fetch a YouTube video's transcript (captions/subtitles) and save a clean single-line .txt file using yt-dlp. Use whenever the user needs a video transcript — "get the transcript", "transcript of this video", "pull the captions", "download subtitles", "what does this YouTube video say". Pure yt-dlp, no API keys; requires yt-dlp on PATH (see Setup). NOT for downloading videos/audio or Whisper transcription unless the user explicitly asks.
---

# YouTube Transcript (yt-dlp)

Fetch a YouTube video's transcript and save a clean raw `.txt` file. Pure local yt-dlp — no API keys, no third-party services.

## Setup (one-time)

- `yt-dlp` must be on PATH. Check: `yt-dlp --version`
- Install: `python -m pip install yt-dlp` (Python's `Scripts/` dir must be on PATH)
- **Self-updates are OFF by user preference — never run `yt-dlp -U` or any auto-update.** Updates happen only when the user explicitly asks: `python -m pip install -U yt-dlp`
- Node is required for the scripts (`--js-runtimes node` is used on every yt-dlp call — deno is the default; node must be enabled explicitly).
- ffmpeg and browser impersonation are NOT required for captions. Warnings about missing ffmpeg or unavailable impersonation targets are benign — ignore them.

## Save location

- Always `b0ttsagent/temp/youtube-transcripts/` in the project root (the folder containing `.agents/` with this skill). The script creates it — no manual `mkdir` needed.
- Filename: `Channel_Title` (spaces → `_`), sanitized for Windows and truncated to 100 chars; falls back to the video ID if metadata is unavailable.

## Usage

Run the orchestrator script — it anchors to the project root itself, so it works from any cwd:

```bash
bash "<this-skill-dir>/scripts/transcript.sh" "<video url>"                          # English captions
bash "<this-skill-dir>/scripts/transcript.sh" "<video url>" "de"                     # exact language codes
bash "<this-skill-dir>/scripts/transcript.sh" "<video url>" "en,en-orig" "chrome"    # bot-flag workaround (cookies)
```

The script: pre-flights `yt-dlp` + `node`, derives the filename, downloads captions, flattens via `scripts/flatten-json3.js`, and prints the saved `.txt` path. It prefers native **manual** English captions (`en`) over native **auto** (`en-orig`) — exact language codes only.

## Non-English / no-match videos

Run `yt-dlp --js-runtimes node --no-playlist --list-subs --skip-download "<url>"` to see the available tracks, then re-run the script with the exact code, e.g. `"de"` or `"en-US"`. Always exact codes, never wildcards.

## Bot-flag / 429 & 403 handling

`HTTP 429`, `HTTP 403`, or "Sign in to confirm you're not a bot" = IP flagged. **NEVER retry in a loop** (makes it worse). Instead:

1. Stop.
2. Re-run the script with a browser once: `"chrome"`, then `"vivaldi"`, then `"edge"` — skipping any that error (a running browser may lock its cookie DB; just try the next).
3. Still failing → stop and tell the user.

The script also warns when YouTube flags only *some* caption tracks (e.g. the auto track) — the transcript may still be complete; re-run with cookies if it looks incomplete.

## Failure handling

- Transient failure (network hiccup): retry once as-is, then stop and report. No `-U`, no loops.
- The script's error messages are targeted: missing tools → install command; bot-flag → cookies re-run; no captions → `--list-subs` hint or "genuinely no captions"; odd extraction errors → outdated-yt-dlp hint (manual update only).
- Whisper/audio transcription is out of scope unless the user explicitly asks.

## Output

Report the saved `.txt` path; print the text if it's short.
