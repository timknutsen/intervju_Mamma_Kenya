#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -lt 1 ]; then
  echo "Usage: scripts/transcribe_local.sh <audio-file> [model]" >&2
  exit 1
fi

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_BIN="$ROOT_DIR/.venv/bin"
OUTPUT_DIR="$ROOT_DIR/outputs"
MODEL="${2:-mlx-community/whisper-large-v3-turbo}"
AUDIO_FILE="$1"

mkdir -p "$OUTPUT_DIR"

# Ensure the conda-installed ffmpeg binary is visible to the transcription tool.
export PATH="$HOME/miniforge3/bin:$PATH"

"$VENV_BIN/mlx_whisper" \
  "$AUDIO_FILE" \
  --model "$MODEL" \
  --output-dir "$OUTPUT_DIR" \
  --output-format all \
  --task transcribe \
  --language Norwegian \
  --word-timestamps True \
  --verbose False
