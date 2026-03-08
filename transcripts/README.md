# Transcript workflow

This folder now holds the source-language transcript support layer for the full interview project.

## Where we are

At the moment, this folder contains the strongest source-near versions of the interviews, mostly in Norwegian, built from the raw recordings and machine transcription outputs.

Current files:

- `del-1-master-transcript.md`: preservation-first source transcript for `Mamma I kenya del 1.m4a`
- `del-2-master-transcript.md`: preservation-first source transcript for `Mamma oppvekst Kenya del 2.m4a`
- `del-3-master-transcript.md`: preservation-first source transcript for `mamma livet etter Afrika del 3.m4a`
- `mau-mau-side-master-transcript.md`: standalone side transcript for `Mamma intervju Sidespor 1 - Mau Mau.m4a`
- `del-1-open-questions.md`, `del-2-open-questions.md`, `del-3-open-questions.md`: legacy compatibility files that now point back to the verification lists inside the master transcripts

## Where we are going

These transcript files are no longer the final editorial master layer.

From now on, they serve three purposes:

1. preserve the original source-language shape of the interviews
2. support verification with your mother
3. feed the canonical English interview-faithful master that will be built next

That English interview-faithful master should:

- stay as close as possible to what was actually said
- remain formatted as an interview
- be cleaned only enough to remove obvious repetition, filler, and ASR noise
- be the main base for all later story versions

## Standard

These are not neat summary documents. They are faithful edited transcript-support files.

- Preserve psychology, family dynamics, anecdotes, atmosphere, humor, contradiction, and uncertainty.
- Keep meaningful digressions when they add character, memory texture, or historical context.
- Fix obvious ASR mistakes and punctuation failures.
- Remove filler only when it does not carry meaning or rhythm.
- Mark unresolved names, dates, and places explicitly.
- End each master transcript with `Preservation notes` and `Verification list`.
- Keep the material traceable to the audio so later English work can stay honest.

## Machine transcript sources

Machine outputs live in `outputs/` and are source material only.

- `.txt`: fastest file to read while drafting
- `.json`: useful when checking segment boundaries or word timing
- `.srt` / `.vtt`: useful when verifying sequence and timing
- `.tsv`: useful for lightweight timing review

Do not treat the machine outputs as final deliverables.
