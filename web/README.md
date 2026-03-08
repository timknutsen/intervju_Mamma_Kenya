# Web workflow

The review site is built from the English source files in `stories/en/`.

Current deployment status:

- the repo is pushed to GitHub
- the site output lives in `docs/`
- GitHub Pages should serve the site from `main` + `/docs`
- the current site is plain static HTML and CSS generated locally, not Jekyll

Build command:

```bash
python3 scripts/build_review_site.py
```

Published output:

- `docs/` contains the GitHub Pages-ready static site

Current purpose:

- let family review the three English layers side by side
- keep the site reproducible from the current source texts
- delay richer interactive work until the text stack is more stable

Current recommendation:

- keep the plain static Pages setup
- do not add Jekyll or GitHub Actions yet
- evolve the site only as the text stack and review needs become clearer
