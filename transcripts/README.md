# Transcript workflow

This folder holds the human-edited transcript layer for the full interview project.

## Files

- `del-1-master-transcript.md`: cleaned transcript for `Mamma I kenya del 1.m4a`
- `del-1-open-questions.md`: unresolved names, dates, places, and wording from del 1
- `del-2-master-transcript.md`: cleaned transcript for `Mamma oppvekst Kenya del 2.m4a`, including the Mau Mau side recording as a marked supplemental section
- `del-2-open-questions.md`: unresolved items from del 2 and the supplemental Mau Mau recording
- `del-3-master-transcript.md`: cleaned transcript for `mamma livet etter Afrika del 3.m4a`
- `del-3-open-questions.md`: unresolved names, dates, places, and wording from del 3

## Cleanup standard

- Preserve spoken Norwegian voice and speaker order.
- Fix obvious ASR mistakes and punctuation failures.
- Remove only distracting filler or repetition.
- Mark uncertain words or names explicitly.
- Add light timestamps at section starts and major topic shifts.

## Machine transcript sources

Machine outputs live in `outputs/` and are source material only.

- `.txt`: fastest file to read while drafting
- `.json`: useful when checking segment boundaries or word timing
- `.srt` / `.vtt`: useful when verifying sequence and timing
- `.tsv`: useful for lightweight timing review

Do not treat the machine outputs as final deliverables.
