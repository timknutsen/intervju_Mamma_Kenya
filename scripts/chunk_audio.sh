#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -lt 1 ] || [ "$#" -gt 2 ]; then
  echo "Usage: scripts/chunk_audio.sh <audio-file> [chunk-seconds]" >&2
  exit 1
fi

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
AUDIO_FILE="$1"
CHUNK_SECONDS="${2:-900}"

if [ ! -f "$AUDIO_FILE" ]; then
  echo "Audio file not found: $AUDIO_FILE" >&2
  exit 1
fi

STEM="$(basename "$AUDIO_FILE")"
STEM="${STEM%.*}"
SLUG="$(printf '%s' "$STEM" | tr '[:upper:]' '[:lower:]' | sed -E 's/[^a-z0-9]+/-/g; s/^-+//; s/-+$//')"
CHUNK_DIR="$ROOT_DIR/outputs/chunks/$SLUG"

mkdir -p "$CHUNK_DIR"

export PATH="$HOME/miniforge3/bin:$PATH"

ffmpeg \
  -i "$AUDIO_FILE" \
  -f segment \
  -segment_time "$CHUNK_SECONDS" \
  -c copy \
  -reset_timestamps 1 \
  "$CHUNK_DIR/${SLUG}-part-%02d.m4a"

echo "$CHUNK_DIR"
