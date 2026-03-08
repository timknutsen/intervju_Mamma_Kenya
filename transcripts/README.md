# Transcript workflow

This folder holds the source-language transcript support layer for the interview project.

## Active role

These files are not the final editorial master. Their job is to:

1. preserve the source-language shape of the interviews
2. support verification against the raw recordings
3. support the active English master files in `stories/en/`

Current active files:

- `del-1-master-transcript.md`
- `del-2-master-transcript.md`
- `del-3-master-transcript.md`
- `mau-mau-side-master-transcript.md`

## Standard

These are preservation-first support documents, not polished summaries.

- Keep psychology, anecdotes, atmosphere, contradiction, and uncertainty.
- Fix obvious ASR mistakes and punctuation failures.
- Remove filler only when it adds no meaning or rhythm.
- Mark unresolved names, dates, and places explicitly.
- End each master transcript with `Preservation notes` and `Verification list`.
- Keep the material traceable to the audio so the English stack stays honest.

## Machine transcript sources

Machine outputs live in `outputs/` and are source material only.

- `.txt`: fastest file to read while drafting and checking wording
- `.json`: useful when checking segment boundaries and recovering degraded passages

Other machine formats are intentionally not kept in the active repo. They can be regenerated from the transcription scripts if needed.
