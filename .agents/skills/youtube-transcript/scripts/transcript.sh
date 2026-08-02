#!/usr/bin/env bash
# YouTube transcript fetcher — part of the youtube-transcript skill.
# Usage:
#   bash transcript.sh "<URL>"                       # English captions (default)
#   bash transcript.sh "<URL>" "<langs>"             # exact caption codes, e.g. "de" or "en-US"
#   bash transcript.sh "<URL>" "<langs>" "<browser>" # bot-flag workaround: --cookies-from-browser
# Saves to <project-root>/b0ttsagent/temp/youtube-transcripts/<Channel_Title>.txt
set -u

URL="${1:?usage: transcript.sh <URL> [langs] [browser]}"
SUB_LANGS="${2:-en,en-orig}"
BROWSER="${3:-}"

# Anchor to the project root via this script's own location — works from any cwd.
SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SKILL_DIR/../../../.." && pwd)"
OUT="$ROOT/b0ttsagent/temp/youtube-transcripts"
mkdir -p "$OUT"

# Pre-flight — fail loudly; never auto-install (installs are manual by user preference).
command -v yt-dlp >/dev/null 2>&1 || { echo "ERROR: yt-dlp is not installed. Install it with: python -m pip install yt-dlp"; exit 1; }
command -v node   >/dev/null 2>&1 || { echo "ERROR: node is not installed — required for the flattener."; exit 1; }

COOKIES=""
[ -n "$BROWSER" ] && COOKIES="--cookies-from-browser $BROWSER"
YTDLP="yt-dlp --js-runtimes node --no-playlist --sleep-requests 1 $COOKIES"

# --- Filename: Channel_Title (channel -> uploader -> uploader_id fallback) ---
META=$($YTDLP --print "%(channel,uploader,uploader_id)s|%(title)s" --skip-download "$URL" 2>/dev/null)
NAME=$(node "$SKILL_DIR/slugify.js" "$META")
if [ -z "$NAME" ]; then
  NAME=$(node "$SKILL_DIR/slugify.js" "$($YTDLP --print "%(id)s" --skip-download "$URL" 2>/dev/null)")
fi
if [ -z "$NAME" ]; then
  echo "ERROR: could not fetch video metadata — check the URL."
  echo "  If this is a 429/403 bot-flag, re-run with: $0 \"$URL\" \"$SUB_LANGS\" chrome"
  echo "  If yt-dlp errors look odd, it may be outdated — update manually (never auto): python -m pip install -U yt-dlp"
  exit 1
fi
echo "Fetching captions for: $NAME"

# --- Download captions. Exact language codes only — a wildcard (en.*) bursts 429s. ---
DL_OUT=$($YTDLP --skip-download --write-subs --write-auto-subs \
  --sub-langs "$SUB_LANGS" --sub-format json3 \
  -o "$OUT/$NAME.%(ext)s" "$URL" 2>&1)

# --- Pick the caption file: manual <primary lang> > auto <primary lang> > anything written ---
PRIMARY=$(printf '%s' "$SUB_LANGS" | cut -d, -f1)
JSON3=""
for cand in "$NAME.$PRIMARY.json3" "$NAME.$PRIMARY-orig.json3"; do
  [ -f "$OUT/$cand" ] && JSON3="$OUT/$cand" && break
done
[ -z "$JSON3" ] && JSON3=$(ls "$OUT"/"$NAME".*.json3 2>/dev/null | head -1)

if [ -z "$JSON3" ]; then
  echo "NOTE: no captions written for language(s) '$SUB_LANGS'."
  echo "  - Other languages? List them with: $YTDLP --list-subs --skip-download \"$URL\" — then re-run with the exact code."
  echo "  - The video may genuinely have no captions."
  if echo "$DL_OUT" | grep -qiE "429|sign in to confirm|403"; then
    echo "  - YouTube flagged this IP (429/403). Re-run with: $0 \"$URL\" \"$SUB_LANGS\" chrome"
  fi
  exit 1
fi

# --- Flatten to a clean single-line .txt ---
node "$SKILL_DIR/flatten-json3.js" "$JSON3" "$OUT/$NAME.txt"

# --- Warn about partial flags (e.g. auto track blocked) so the user can re-run if needed ---
if echo "$DL_OUT" | grep -qiE "429|sign in to confirm|403"; then
  echo "NOTE: YouTube flagged some caption tracks (429/403) — the transcript above may be missing the auto track."
  echo "  If it looks incomplete, re-run with: $0 \"$URL\" \"$SUB_LANGS\" chrome"
fi
