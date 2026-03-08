# Transcript workflow

This folder holds the preservation-first transcript layer for the full interview project.

## Files

- `del-1-master-transcript.md`: preservation-first transcript for `Mamma I kenya del 1.m4a`
- `del-2-master-transcript.md`: preservation-first transcript for `Mamma oppvekst Kenya del 2.m4a`
- `del-3-master-transcript.md`: preservation-first transcript for `mamma livet etter Afrika del 3.m4a`
- `mau-mau-side-master-transcript.md`: standalone side transcript for `Mamma intervju Sidespor 1 - Mau Mau.m4a`
- `del-1-open-questions.md`, `del-2-open-questions.md`, `del-3-open-questions.md`: legacy compatibility files that now point back to the verification lists inside the master transcripts

## Standard

These are not neat summary documents. They are faithful edited transcripts.

- Preserve psychology, family dynamics, anecdotes, atmosphere, humor, contradiction, and uncertainty.
- Keep meaningful digressions when they add character, memory texture, or historical context.
- Fix obvious ASR mistakes and punctuation failures.
- Remove filler only when it does not carry meaning or rhythm.
- Mark unresolved names, dates, and places explicitly.
- End each master transcript with `Preservation notes` and `Verification list`.

## Machine transcript sources

Machine outputs live in `outputs/` and are source material only.

- `.txt`: fastest file to read while drafting
- `.json`: useful when checking segment boundaries or word timing
- `.srt` / `.vtt`: useful when verifying sequence and timing
- `.tsv`: useful for lightweight timing review

Do not treat the machine outputs as final deliverables.
