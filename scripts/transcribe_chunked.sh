#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -lt 1 ] || [ "$#" -gt 2 ]; then
  echo "Usage: scripts/transcribe_chunked.sh <audio-file> [model]" >&2
  exit 1
fi

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
AUDIO_FILE="$1"
MODEL="${2:-mlx-community/whisper-large-v3-turbo}"

CHUNK_DIR="$("$ROOT_DIR/scripts/chunk_audio.sh" "$AUDIO_FILE")"

for chunk in "$CHUNK_DIR"/*.m4a; do
  if [ ! -e "$chunk" ]; then
    echo "No chunk files found in $CHUNK_DIR" >&2
    exit 1
  fi
  "$ROOT_DIR/scripts/transcribe_local.sh" "$chunk" "$MODEL"
done

echo "$CHUNK_DIR"
