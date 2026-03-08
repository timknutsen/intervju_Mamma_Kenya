# Repository Guidelines

## Mission and current direction
This repository is an oral-history production workspace for documenting, preserving, shaping, and eventually publishing your mother's story of growing up in colonial Kenya.

The workflow has changed in an important way:

1. English is now the working language for all active drafting and editorial work.
2. The most faithful interview-near version should also become an English master file.
3. Norwegian is now a late-stage publication and review layer, not the drafting master.
4. The long-term publication target is a website, likely served through GitHub Pages, so your mother can read and comment as the project evolves.

The repo is currently in a transition state:

- The raw source material is the original Norwegian-language interview audio.
- The preservation-first transcript layer currently exists mainly in Norwegian.
- There is already a Norwegian working draft, an English interview-faithful draft, and English narrative drafts in progress.
- These are useful working artifacts, but they are no longer the final workflow model.

The target workflow from now on is:

1. Build an English interview-faithful master transcript that stays as close as possible to what was actually said, while cleaning obvious ASR errors, filler, and repetition.
2. Build an English story-faithful version that tells the material as your mother told it.
3. Build an English story-optimized version that improves flow, chronology, transitions, and literary force.
4. Only after those English versions are strong and approved should Norwegian publication versions be produced.
5. Publish approved versions on a web page for iterative review, then later expand that into the richer interactive experience.

Do not drift back into treating Norwegian as the drafting master unless the user explicitly asks for that.

## Source hierarchy and workflow contracts
Future agents must respect this artifact hierarchy:

1. Raw audio in the repository root is immutable source material.
2. Machine transcription outputs are intermediate artifacts only.
3. Source-language cleaned transcripts are support documents for verification and traceability.
4. The English interview-faithful master is the canonical editorial base.
5. The English story-faithful narrative is the second layer.
6. The English story-optimized narrative is the third layer.
7. Norwegian versions are downstream adaptations from approved English layers.
8. The website and later interactive experience are downstream from approved text, research, and media.

Treat these as explicit interfaces between phases:

- Audio processing -> source-language transcript support.
- Source-language transcript support -> English interview-faithful master.
- English interview-faithful master -> English story-faithful version.
- English story-faithful version -> English story-optimized version.
- Approved English versions -> Norwegian publication versions.
- Approved text, research, and media -> website and later interactive experience.

Research notes support the story but do not replace interview content. Media inventories are required support records for externally sourced photos, maps, and videos.

## Project structure and file roles
Keep raw `.m4a` recordings in the repository root only when they are primary source material. Use clear folders for everything derived from them.

- `transcripts/`: source-language transcript support, verification artifacts, timestamped notes, and unresolved passage lists.
- `stories/en/`: the active master story layer in English.
- `stories/no/`: late-stage Norwegian adaptations derived from approved English versions.
- `research/`: sourced historical notes, chronology, geography, colonial context, Thika context, plantation life notes, and citation logs.
- `assets/family/`: family-provided photos and media.
- `assets/historical/`: curated historical media from archives or the web, with source and rights notes.
- `outputs/`: machine transcription outputs and generated review/export files.
- `web/`: future GitHub Pages site and, later, richer interactive web work.
- `scripts/`: repeatable local tooling such as transcription and export generation.

If a needed folder does not exist yet, create it before adding new derived material. Avoid scattering working files in the repository root.

## Session startup rules
At the start of every work session:

1. Review the current state of transcripts, English story versions, Norwegian adaptations, research, and media inventories.
2. Identify the highest-priority unfinished layer and continue that before expanding scope.
3. Surface unresolved names, dates, places, chronology gaps, speaker ambiguities, and uncertain wording.
4. Avoid jumping into web polish or historical context buildout while the English master text stack is still unstable.

Always state which layer you are working on: transcript support, English interview-faithful master, English story-faithful narrative, English story-optimized narrative, Norwegian adaptation, research/context, media archive, or web experience.

## Transcript rules
The interview-faithful master is the most important artifact in this repository, even though the raw interview happened in Norwegian.

From now on, transcript work should distinguish clearly between two things:

- source-language transcript support inside `transcripts/`
- the canonical English interview-faithful master that will be built from it

Rules for the interview-faithful master:

- Keep it as close as possible to what was actually said.
- Preserve speaker order, sequence, uncertainty, tone, and distinctive storytelling voice.
- Preserve psychology, family dynamics, revealing side remarks, humor, contradiction, and vivid anecdotes.
- Preserve colonial and social atmosphere, everyday routines, labor structures, travel details, and domestic texture.
- Fix obvious ASR errors and remove filler only when it does not carry meaning, rhythm, or character.
- Do not silently invent missing words, chronology, names, motives, or historical claims.
- Mark uncertain passages explicitly for later review with your mother using labels such as `[uncertain]`, `[name unclear]`, or `[year uncertain]`.
- Keep it formatted as an interview so it is easy to follow and recognizably close to what was actually said.
- Your mother should be able to recognize this version as the closest cleaned form of the real interview.

Rules for source-language transcript support in `transcripts/`:

- Keep it preservation-first and traceable to the audio.
- Use it to resolve wording, sequence, names, and speaker flow.
- Do not mistake it for the final canonical publication base now that English is the working master.

The Mau Mau side recording should exist as its own standalone transcript artifact and also be linked from the relevant main interview section.

## Story-writing rules
Story work now proceeds in three explicit English versions.

### Version 1: interview-faithful

- Closest possible cleaned version of what was said.
- Still in interview form.
- Minimal restructuring.
- Designed for your mother to recognize the conversation.

### Version 2: story-faithful

- Tell the material as your mother told it.
- Preserve her way of moving through memory, emphasis, irony, and anecdote.
- Closer to memoir prose than transcript, but still clearly hers.

### Version 3: story-optimized

- Improve flow, chronology, transitions, and literary force.
- Restructure where needed for clarity and emotional movement.
- Keep the voice recognizable and defensible from the earlier layers.

Only after those three English layers are stable should Norwegian versions be created.

For all story work:

- Keep your mother's way of telling stories recognizable.
- Improve flow, chronology, transitions, and language without flattening her character or rhythm.
- Narrative restructuring is allowed only when it remains clearly traceable to the earlier layers.
- Separate remembered family experience from researched historical context.
- If a sentence or scene is inferred, condensed, or reordered for clarity, that should be defensible from the transcript stack.

The goal is not literal transcription and not free invention. The goal is a set of increasingly shaped narrative versions that still feel like they come from her.

## Research and sourcing rules
Historical research is important, but it must remain clearly separated from family memory.

- Use outside sources to support chronology, geography, political context, plantation life, Thika, colonial Kenya, and the Mau Mau period.
- Maintain a hard distinction between what comes from the interview and what comes from sources.
- Record citations and access dates for historical claims that are not directly from the interview.
- Prefer primary or high-quality institutional sources for contested historical material.
- If research contradicts memory, preserve the memory in the transcript/story layer and note the tension explicitly in research or editorial notes.

Do not let sourced history overwrite lived memory without making that editorial move explicit.

## Media and web publishing rules
The publication path now has two stages:

1. Publish readable review versions on a website, likely via GitHub Pages, so your mother can read and respond.
2. Over time, expand that into the richer museum-like interactive experience.

Rules:

- Default platform direction is web-first.
- Near-term web goal is review and iteration, not polish for its own sake.
- Do not lock the repository to a complex framework until the text stack is more stable.
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
- `mkdir -p transcripts stories/en stories/no research assets/family assets/historical web`: create the standard working structure when needed.

If additional scripts are added later, document their exact invocation here and keep commands reproducible from the repository root.

## Naming and writing conventions
Use descriptive, consistent filenames. Prefer lowercase, hyphen-separated names for new derived files, such as:

- `transcripts/del-1-master-transcript.md`
- `stories/en/interview-faithful-v1.md`
- `stories/en/story-faithful-v1.md`
- `stories/en/story-optimized-v1.md`
- `stories/no/intervju-naer-v1.md`
- `stories/no/historie-som-fortalt-v1.md`
- `stories/no/historie-optimalisert-v1.md`
- `research/thika-colonial-context.md`
- `assets/historical/media-inventory.md`

Preserve original recording filenames unless there is a strong archival reason to rename them. For Markdown, use short sections, sentence-case headings, concise bullets, and clear separation between transcript text, editorial notes, preservation notes, and verification lists.

When drafting in English, keep the language natural, direct, and literary where appropriate, but preserve your mother's voice.

## Verification guidelines
Because this repository is archival and editorial rather than executable, verification means checking accuracy, traceability, and organization.

- Confirm raw recordings remain untouched.
- Check that transcript or story filenames clearly map back to the source material.
- Spot-check source-language transcripts against the recording, especially names, dates, and uncertain passages.
- Confirm that the English interview-faithful master stays close to the actual interview.
- Confirm that the story-faithful and story-optimized versions remain traceable to the earlier layers.
- Confirm that Norwegian versions are adapted from approved English layers, not rebuilt independently.
- Confirm that sourced historical claims include citations and access dates.
- Confirm that external media records include credit and rights or reuse notes.
- Before major web work, verify that the English master stack is strong enough for publication review.

## Commit and pull request guidelines
Git history is available locally now, but keep commit messages short and imperative, such as:

- `Add interview-faithful English master draft`
- `Revise story-faithful English version`
- `Document English-first workflow`
- `Prepare GitHub Pages review structure`

For pull requests, include:

- A brief summary of what was advanced in the workflow.
- A file list covering new transcripts, story versions, research notes, media records, or web work.
- Any manual verification performed, such as playback checks, timestamp review, citation review, or story-to-source trace checks.

## Archive and safety notes
Treat the `.m4a` files as source material and do not overwrite or compress originals in place.

- Keep raw recordings separate from transcripts, stories, research, and exports.
- Keep machine transcription output separate from cleaned transcript work.
- Keep research notes separate from story manuscripts.
- Keep family media separate from externally sourced historical media.
- Do not present inferred or researched material as if it came directly from your mother.
- Do not let later story polish erase the existence of the more faithful earlier layers.
