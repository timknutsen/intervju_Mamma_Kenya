# Repository Guidelines

## Mission and workflow
This repository is an oral-history production workspace for documenting and shaping your mother's story of growing up in colonial Kenya. The work should proceed in three layers, in this order:

1. Build a faithful, cleaned, full interview transcript from the raw recordings.
2. Use that transcript as the base for a Norwegian narrative story, then an English adaptation.
3. Build a web-based interactive experience over time, using approved story text, approved research context, and curated media.

The current priority is the cleaned full interview transcript. Do not treat one-off PDF prototypes as the main goal.

## Source hierarchy and workflow contracts
Future agents must respect this artifact hierarchy:

1. Raw audio in the repository root is immutable source material.
2. Machine transcription outputs are intermediate artifacts only.
3. The cleaned full interview transcript is the authoritative textual base.
4. The Norwegian story manuscript is the primary literary adaptation.
5. The English story is an adaptation of the Norwegian story and transcript, not an independent rewrite.
6. The interactive web experience is downstream from the approved transcript, story, research, and media layers.

Treat these as explicit interfaces between phases:

- Audio processing -> cleaned transcript.
- Cleaned transcript -> Norwegian story manuscript.
- Norwegian story manuscript -> English adaptation.
- Approved text, research, and media -> interactive web experience.

Research notes support the story but do not replace interview content. Media inventories are required support records for externally sourced photos, maps, and videos.

## Project structure and file roles
Keep raw `.m4a` recordings in the repository root only when they are primary source material. Use clear folders for everything derived from them.

- `transcripts/`: cleaned interview transcripts, transcript review drafts, timestamped notes, and unresolved passage lists.
- `stories/no/`: Norwegian story manuscripts and revision drafts.
- `stories/en/`: English adaptations derived from the Norwegian story and transcript.
- `research/`: sourced historical notes, chronology, geography, colonial context, Thika context, plantation life notes, and citation logs.
- `assets/family/`: family-provided photos and media.
- `assets/historical/`: curated historical media from archives or the web, with source and rights notes.
- `outputs/`: machine transcription outputs and generated review/export files.
- `web/`: future interactive experience source when that phase becomes active.
- `scripts/`: repeatable local tooling such as transcription and export generation.

If a needed folder does not exist yet, create it before adding new derived material. Avoid scattering working files in the repository root.

## Session startup rules
At the start of every work session:

1. Review the current state of transcripts, stories, research, and media inventories.
2. Identify the highest-priority unfinished layer and continue that before expanding scope.
3. Surface unresolved names, dates, places, chronology gaps, speaker ambiguities, and uncertain wording.
4. Avoid jumping into interactive polish while transcript and story foundations are incomplete.

Always state which layer you are working on: transcript, story, research/context, media archive, or interactive experience.

## Transcript rules
The cleaned full interview transcript is the most important artifact in this repository.

- Aim for faithful-but-readable cleanup.
- Preserve speaker order, sequence, uncertainty, tone, and distinctive storytelling voice.
- Fix obvious ASR errors and remove only distracting filler or repetition.
- Do not silently invent missing words, chronology, names, or historical claims.
- Mark uncertain passages explicitly for later review with your mother.
- Keep the transcript traceable to the source audio.
- When possible, preserve timestamps or other links back to the raw recording for difficult passages.

This transcript should read clearly, but it must still feel like the real conversation.

## Story-writing rules
Story work begins only after there is a usable cleaned transcript for the relevant section.

- The Norwegian story is the master narrative version.
- The English story is an adaptation of the Norwegian story and transcript.
- Keep your mother's way of telling stories recognizable.
- Improve flow, chronology, transitions, and language without flattening her character or rhythm.
- Narrative restructuring is allowed only when it remains clearly traceable to the transcript.
- Separate remembered family experience from researched historical context.
- If a sentence or scene is inferred, condensed, or reordered for clarity, that should be defensible from the transcript.

The goal is not literal transcription and not free invention. The goal is a strong literary narrative that still sounds like your mother could have told it that way.

## Research and sourcing rules
Historical research is important, but it must remain clearly separated from family memory.

- Use outside sources to support chronology, geography, political context, plantation life, Thika, colonial Kenya, and the Mau Mau period.
- Maintain a hard distinction between what comes from the interview and what comes from sources.
- Record citations and access dates for historical claims that are not directly from the interview.
- Prefer primary or high-quality institutional sources for contested historical material.
- If research contradicts memory, preserve the memory in the transcript/story layer and note the tension explicitly in research or editorial notes.

Do not let sourced history overwrite lived memory without making that editorial move explicit.

## Media and interactive experience rules
The long-term goal is a powerful, museum-like interactive experience built slowly and carefully.

- Default platform direction is web-first.
- Do not lock the repository to a specific framework until the transcript and story foundations are stronger.
- The final experience should combine approved story text, researched context, maps, timelines, family photos, and carefully curated historical media.
- Family photos should be treated as the emotional core of the experience.
- Historical web-sourced photos, maps, and video clips must be curated carefully with credit, source URL, and reuse or rights notes.
- The experience should prioritize depth, atmosphere, chronology, and historical grounding over fast prototyping.

Assume this part of the project will be iterative and built over time.

## Build, test, and development commands
There is no conventional build system yet for the repository as a whole, but there is a local transcription workflow and a growing content pipeline.

- `ls -lh *.m4a`: review recording filenames and file sizes.
- `ffprobe "Mamma I kenya del 1.m4a"`: inspect audio metadata if `ffmpeg` is installed.
- `scripts/transcribe_local.sh "<audio-file>"`: generate machine transcription outputs in `outputs/`.
- `scripts/transcribe_chunked.sh "<audio-file>"`: chunk a long recording into 15-minute parts and transcribe each chunk with the same local setup.
- `scripts/chunk_audio.sh "<audio-file>"`: create fallback chunk files in `outputs/chunks/` without transcribing them.
- `mkdir -p transcripts stories/no stories/en research assets/family assets/historical web`: create the standard working structure when needed.

If additional scripts are added later, document their exact invocation here and keep commands reproducible from the repository root.

## Naming and writing conventions
Use descriptive, consistent filenames. Prefer lowercase, hyphen-separated names for new derived files, such as:

- `transcripts/del-1-cleaned.md`
- `transcripts/del-2-open-questions.md`
- `stories/no/mors-oppvekst-i-kenya-v1.md`
- `stories/en/mothers-childhood-in-kenya-v1.md`
- `research/thika-colonial-context.md`
- `assets/historical/media-inventory.md`

Preserve original recording filenames unless there is a strong archival reason to rename them. For Markdown, use short sections, sentence-case headings, concise bullets, and clear separation between transcript text, editorial notes, and research notes.

## Verification guidelines
Because this repository is archival and editorial rather than executable, verification means checking accuracy, traceability, and organization.

- Confirm raw recordings remain untouched.
- Check that transcript or story filenames clearly map back to the source material.
- Spot-check cleaned transcripts against the recording, especially names, dates, and uncertain passages.
- Confirm that story drafts remain traceable to the transcript.
- Confirm that sourced historical claims include citations and access dates.
- Confirm that external media records include credit and rights or reuse notes.
- Before major story or interactive work, verify that transcript foundations are strong enough for the next layer.

## Commit and pull request guidelines
Git history is not available in the current workspace, so no local commit convention can be inferred. Use short, imperative commit messages such as `Add cleaned transcript for del 1` or `Create Norwegian story draft from transcript`.

For pull requests, include:

- A brief summary of what was advanced in the workflow.
- A file list covering new transcripts, stories, research notes, media records, or web work.
- Any manual verification performed, such as playback checks, timestamp review, citation review, or story-to-transcript trace checks.

## Archive and safety notes
Treat the `.m4a` files as source material and do not overwrite or compress originals in place.

- Keep raw recordings separate from transcripts, stories, research, and exports.
- Keep machine transcription output separate from cleaned transcript work.
- Keep research notes separate from story manuscripts.
- Keep family media separate from externally sourced historical media.
- Do not present inferred or researched material as if it came directly from your mother.
