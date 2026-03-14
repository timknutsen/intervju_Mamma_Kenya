#!/usr/bin/env python3
from __future__ import annotations

import html
import re
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

PAGES = [
    {
        "slug": "interview-faithful",
        "title": "Interview-Faithful",
        "source": ROOT / "stories/en/interview-faithful-v1.md",
        "summary": "The closest practical English version of the original interview, still in interview form.",
        "feedback": "Ask whether this still sounds like the real conversation and whether any important wording or tone has drifted.",
    },
    {
        "slug": "story-faithful",
        "title": "Story-Faithful",
        "source": ROOT / "stories/en/story-faithful-v1.md",
        "summary": "A memoir-like retelling that follows the way she tells the story.",
        "feedback": "Ask whether this feels like her natural way of telling the story, including digressions, emphasis, and emotional tone.",
    },
    {
        "slug": "story-optimized",
        "title": "Story-Optimized",
        "source": ROOT / "stories/en/story-optimized-v1.md",
        "summary": "A more shaped narrative with stronger chronology, transitions, and pacing.",
        "feedback": "Ask whether the reshaping improves the reading experience without losing her personality, complexity, or truthfulness.",
    },
]

SITE_LINKS = [
    {"href": "index.html", "label": "Story"},
    {"href": "history.html", "label": "Historical Context"},
    {"href": "integrated.html", "label": "The Full Story"},
]


def inline_markup(text: str) -> str:
    escaped = html.escape(text, quote=False)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", escaped)
    return escaped


def flush_paragraph(parts: list[str], blocks: list[str]) -> None:
    if not parts:
        return
    paragraph = " ".join(part.strip() for part in parts if part.strip())
    if paragraph:
        blocks.append(f"<p>{inline_markup(paragraph)}</p>")
    parts.clear()


def flush_list(items: list[str], blocks: list[str]) -> None:
    if not items:
        return
    rendered = "".join(f"<li>{inline_markup(item)}</li>" for item in items)
    blocks.append(f"<ul>{rendered}</ul>")
    items.clear()


def render_markdown(markdown: str) -> str:
    blocks: list[str] = []
    paragraph_parts: list[str] = []
    list_items: list[str] = []

    for raw_line in markdown.splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()

        if not stripped:
            flush_paragraph(paragraph_parts, blocks)
            flush_list(list_items, blocks)
            continue

        if stripped.startswith("#"):
            flush_paragraph(paragraph_parts, blocks)
            flush_list(list_items, blocks)
            level = len(stripped) - len(stripped.lstrip("#"))
            content = stripped[level:].strip()
            if level == 1:
                blocks.append(f"<h1>{inline_markup(content)}</h1>")
            elif level == 2:
                blocks.append(f"<h2>{inline_markup(content)}</h2>")
            elif level == 3:
                blocks.append(f"<h3>{inline_markup(content)}</h3>")
            else:
                blocks.append(f"<h4>{inline_markup(content)}</h4>")
            continue

        if stripped.startswith("- "):
            flush_paragraph(paragraph_parts, blocks)
            list_items.append(stripped[2:].strip())
            continue

        speaker_match = re.match(r"^(Tim|Mamma):\s+(.*)$", stripped)
        if speaker_match:
            flush_paragraph(paragraph_parts, blocks)
            flush_list(list_items, blocks)
            speaker, speech = speaker_match.groups()
            blocks.append(
                "<p class=\"speaker-line\">"
                f"<span class=\"speaker\">{speaker}</span>"
                f"<span class=\"speech\">{inline_markup(speech)}</span>"
                "</p>"
            )
            continue

        paragraph_parts.append(stripped)

    flush_paragraph(paragraph_parts, blocks)
    flush_list(list_items, blocks)
    return "\n".join(blocks)


def page_shell(title: str, body: str, description: str, active_slug: str) -> str:
    site_nav_html = "".join(
        f"<a class=\"nav-link\" href=\"{link['href']}\">{html.escape(link['label'])}</a>"
        for link in SITE_LINKS
    )
    nav_items = []
    nav_items.append("<a class=\"nav-link\" href=\"index.html\">Overview</a>")
    for page in PAGES:
        class_name = "nav-link active" if page["slug"] == active_slug else "nav-link"
        nav_items.append(
            f"<a class=\"{class_name}\" href=\"{page['slug']}.html\">{html.escape(page['title'])}</a>"
        )
    nav_html = "".join(nav_items)

    return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{html.escape(title)} | Kenya Story Review</title>
    <meta name="description" content="{html.escape(description)}">
    <link rel="stylesheet" href="styles.css">
  </head>
  <body>
    <div class="page-shell">
      <header class="site-header">
        <a class="brand" href="index.html">Kenya Story Review</a>
        <nav class="site-nav">{site_nav_html}</nav>
      </header>
      <nav class="sub-nav">{nav_html}</nav>
      <main class="content-shell">
        <aside class="review-note">
          <p class="eyebrow">Review version</p>
          <h1>{html.escape(title)}</h1>
          <p>{html.escape(description)}</p>
        </aside>
        <article class="story-body">
{body}
        </article>
      </main>
    </div>
  </body>
</html>
"""


def build_index() -> None:
    updated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    cards = []
    for page in PAGES:
        cards.append(
            f"""
            <a class="version-card" href="{page['slug']}.html">
              <p class="eyebrow">English layer</p>
              <h2>{html.escape(page['title'])}</h2>
              <p>{html.escape(page['summary'])}</p>
              <p class="feedback-label">Feedback focus</p>
              <p>{html.escape(page['feedback'])}</p>
            </a>
            """
        )

    html_text = f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Kenya Story Review</title>
    <meta name="description" content="Review site for the English versions of the Kenya childhood story.">
    <link rel="stylesheet" href="styles.css">
  </head>
  <body>
    <div class="page-shell">
      <header class="site-header">
        <a class="brand" href="index.html">Kenya Story</a>
        <nav class="site-nav">
          <a class="nav-link active" href="index.html">Story</a>
          <a class="nav-link" href="history.html">Historical Context</a>
          <a class="nav-link" href="integrated.html">The Full Story</a>
        </nav>
      </header>
      <header class="hero">
        <p class="eyebrow">Family review site</p>
        <h1>Mamma's Kenya Story</h1>
        <p class="hero-copy">
          This site presents three English versions of the same material, from closest-to-interview
          to most shaped. The goal is to compare voice, accuracy, and flow before later Norwegian work
          and before building a richer interactive experience.
        </p>
      </header>

      <section class="overview-grid">
        {''.join(cards)}
      </section>

      <section class="review-guide">
        <div class="guide-card">
          <p class="eyebrow">How to review</p>
          <h2>Start with the interview-faithful version</h2>
          <p>Check what sounds right, what sounds wrong, what is missing, and what feels unlike the original conversation.</p>
        </div>
        <div class="guide-card">
          <p class="eyebrow">Then compare</p>
          <h2>Move from story-faithful to story-optimized</h2>
          <p>Notice whether the improvements in flow and clarity still preserve personality, memory texture, and emotional truth.</p>
        </div>
      </section>

      <footer class="site-footer">
        <p>Built from source files in <code>stories/en/</code>.</p>
        <p>Last generated: {updated}</p>
      </footer>
    </div>
  </body>
</html>
"""
    (DOCS / "index.html").write_text(html_text, encoding="utf-8")


def build_pages() -> None:
    for page in PAGES:
        markdown = page["source"].read_text(encoding="utf-8")
        rendered = render_markdown(markdown)
        html_text = page_shell(page["title"], rendered, page["summary"], page["slug"])
        (DOCS / f"{page['slug']}.html").write_text(html_text, encoding="utf-8")


def build_styles() -> None:
    styles = """
:root {
  --paper: #f4efe4;
  --ink: #1d1b18;
  --muted: #5f5646;
  --accent: #36584f;
  --accent-soft: #dde8e2;
  --line: #d7cdbc;
  --card: rgba(255, 250, 243, 0.85);
  --shadow: 0 18px 45px rgba(31, 26, 20, 0.08);
}

* {
  box-sizing: border-box;
}

body {
  margin: 0;
  background:
    radial-gradient(circle at top left, rgba(197, 166, 117, 0.22), transparent 30%),
    radial-gradient(circle at top right, rgba(54, 88, 79, 0.18), transparent 28%),
    linear-gradient(180deg, #fbf6ec 0%, var(--paper) 100%);
  color: var(--ink);
  font-family: "Iowan Old Style", "Palatino Linotype", "Book Antiqua", Georgia, serif;
  line-height: 1.65;
}

a {
  color: inherit;
}

.page-shell {
  width: min(1120px, calc(100vw - 32px));
  margin: 0 auto;
  padding: 24px 0 56px;
}

.hero,
.site-header,
.review-note,
.story-body,
.guide-card,
.version-card {
  background: var(--card);
  backdrop-filter: blur(6px);
  border: 1px solid rgba(255, 255, 255, 0.7);
  box-shadow: var(--shadow);
}

.hero {
  padding: 40px 34px;
  border-radius: 28px;
}

.hero h1,
.review-note h1,
.story-body h1 {
  font-size: clamp(2.2rem, 3vw, 3.6rem);
  line-height: 1.08;
  margin: 0 0 12px;
  letter-spacing: -0.03em;
}

.hero-copy {
  max-width: 62ch;
  color: var(--muted);
  font-size: 1.08rem;
}

.eyebrow,
.feedback-label {
  font-family: "Avenir Next", "Gill Sans", Calibri, sans-serif;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  font-size: 0.74rem;
  color: var(--accent);
  margin: 0 0 10px;
}

.overview-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
  margin-top: 24px;
}

.version-card,
.guide-card {
  display: block;
  padding: 24px;
  border-radius: 22px;
  text-decoration: none;
}

.version-card h2,
.guide-card h2,
.story-body h2 {
  margin: 0 0 12px;
  font-size: clamp(1.4rem, 2vw, 2rem);
  line-height: 1.15;
}

.version-card p:last-child,
.guide-card p:last-child {
  margin-bottom: 0;
}

.review-guide {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 20px;
  margin-top: 24px;
}

.site-footer {
  padding: 24px 4px 0;
  color: var(--muted);
  font-size: 0.95rem;
}

.site-header {
  display: flex;
  gap: 16px;
  align-items: center;
  justify-content: space-between;
  padding: 18px 22px;
  border-radius: 22px;
  margin-bottom: 24px;
}

.brand {
  text-decoration: none;
  font-family: "Avenir Next", "Gill Sans", Calibri, sans-serif;
  font-size: 0.95rem;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.site-nav {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.sub-nav {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin: 0 0 24px;
  padding: 0 4px;
}

.nav-link {
  text-decoration: none;
  font-family: "Avenir Next", "Gill Sans", Calibri, sans-serif;
  font-size: 0.95rem;
  color: var(--muted);
  padding: 8px 12px;
  border-radius: 999px;
}

.nav-link.active {
  background: var(--accent);
  color: #f5f0e7;
}

.content-shell {
  display: grid;
  grid-template-columns: minmax(240px, 300px) minmax(0, 1fr);
  gap: 24px;
  align-items: start;
}

.review-note {
  position: sticky;
  top: 16px;
  padding: 24px;
  border-radius: 24px;
}

.story-body {
  padding: 30px 34px;
  border-radius: 28px;
}

.story-body h1 {
  font-size: clamp(2rem, 2.8vw, 3rem);
  margin-top: 0;
}

.story-body h2 {
  margin-top: 2.1em;
  padding-top: 0.5em;
  border-top: 1px solid var(--line);
}

.story-body h3 {
  margin-top: 1.7em;
  font-size: 1.15rem;
  color: var(--accent);
}

.story-body p,
.story-body ul {
  max-width: 68ch;
}

.story-body ul {
  padding-left: 1.2em;
}

.speaker-line {
  display: grid;
  grid-template-columns: 84px minmax(0, 1fr);
  gap: 12px;
  margin: 0 0 0.95em;
}

.speaker {
  font-family: "Avenir Next", "Gill Sans", Calibri, sans-serif;
  font-weight: 700;
  color: var(--accent);
  text-transform: uppercase;
  letter-spacing: 0.06em;
  font-size: 0.78rem;
  padding-top: 0.35em;
}

.speech {
  display: block;
}

code {
  background: var(--accent-soft);
  padding: 0.1em 0.35em;
  border-radius: 0.35em;
  font-size: 0.92em;
}

@media (max-width: 860px) {
  .content-shell {
    grid-template-columns: 1fr;
  }

  .review-note {
    position: static;
  }
}

@media (max-width: 640px) {
  .page-shell {
    width: min(100vw - 20px, 1120px);
    padding-top: 12px;
  }

  .hero,
  .story-body,
  .review-note,
  .version-card,
  .guide-card {
    padding: 22px 20px;
    border-radius: 22px;
  }

  .site-header {
    align-items: flex-start;
    flex-direction: column;
  }

  .speaker-line {
    grid-template-columns: 1fr;
    gap: 4px;
  }
}
"""
    (DOCS / "styles.css").write_text(styles.strip() + "\n", encoding="utf-8")


def main() -> None:
    DOCS.mkdir(exist_ok=True)
    (DOCS / ".nojekyll").write_text("", encoding="utf-8")
    build_styles()
    build_index()
    build_pages()


if __name__ == "__main__":
    main()
