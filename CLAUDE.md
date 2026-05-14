# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

Static HTML portfolio (no build step, no framework, no package manager) of graded Pokémon TCG cards. Hosted on GitHub Pages. Styling is Bootstrap 5.3.0 from CDN — `css/styles.css` only overrides the index card grid; per the `bootstrap-guidelines` skill, treat custom CSS in card pages as forbidden.

## Running / previewing

- No build, lint, or test commands exist. To preview, open `index.html` directly or serve the directory with any static server (e.g. VS Code Live Server, `python -m http.server`).
- `helper.py` is a standalone CLI (not part of the site) for processing slab photos before authoring a new card page:
  - `python helper.py upload <path>` — resizes (max 1500px) and uploads an image to Cloudinary, prints `URL:<secure_url>`.
  - `python helper.py qr <path>` — reads a QR code from the top 30% of a slab photo (tries pyzbar then OpenCV `QRCodeDetector`).
  - `python helper.py ocr <path>` — runs Tesseract on the top 25% of a slab photo (the grading label area).
  - Reads Cloudinary credentials from `.env` at repo root. Requires `opencv-python`, `pytesseract`, optionally `pyzbar`, plus the `tesseract` binary on PATH.

## Architecture

Two-file mental model: **`index.html`** is the portfolio listing, and **`pages/<slug>.html`** are the individual card descritivos. Adding a card means editing both.

### `index.html`
- Single ~1700-line file. Cards are hand-authored `.list-group-item` blocks inside `<div id="cardList">`. Each block must contain:
  - thumbnail `<img>`, `<h6>` with card name + number, set/rarity `.badge` elements, a grade `.badge`, and a cert link.
  - `onclick` and `onkeypress` handlers pointing to the corresponding `pages/<slug>.html`.
- Search/filter/sort is plain inline JS at the bottom of the file. **Grade detection is regex-based** on the grade badge text: `/(?:GBA|CAPY|Manafix|CGC|ACE|BGS|PSA|BRG)\s+(\d+\.?\d*)/i`. When introducing a new grader, both the `<select id="graderFilter">` and this regex must be updated, or sort-by-grade silently treats the card as 0.
- `enhanceCardLayout()` runs on load and reshapes each `list-group-item` into a grid card (image / tags / title / grade / cert). Keep the column structure (`.col-md-2` image, `.col-md-5` text, `.col-md-2` grade, `.col-md-3` cert) — the function reads those classes.

### `pages/<slug>.html`
- Each page is a substituted copy of `template_pericia.html` (453 lines, ~80 `{{VARIAVEL}}` placeholders). Sections in order: navbar → header → fotos + identificação → graduação → análise de condição (subgrades + barra de progresso + observações por componente) → histórico (accordion) → footer → modals para zoom das fotos.
- The accordion in the "Histórico" section uses ids `collapse1`, `collapse2`, … — these must be unique **within the page** (Bootstrap collapse will glitch otherwise). The first item commonly has `collapse show` to start expanded.
- Photos are hosted on Cloudinary (`res.cloudinary.com/dyhjjms8y/...`); do not commit binary card photos.

### `.claude/skills/`
Five auto-activating skills enforce the above. The most load-bearing is **`pericia-template`** — invoke its workflow whenever creating a new card page; it owns the placeholder list and the badge-color rules. The others (`bootstrap-guidelines`, `codigo-html`, `acessibilidade`, `estrutura-paginas`) are guardrails on HTML quality. Read `.claude/skills/pericia-template/reference.md` for the full placeholder catalog before substituting.

## Project-specific conventions

- **Rarity labels** use mixed PT/EN with the English abbreviation in parentheses: `Ilustração Especial Rara (SAR)`, `Ilustração Rara (AR)`, `Hyper Rare (HR)`, `Shiny Rare (SR)`, `Ultra Rare (UR)`. Use this verbatim in both `index.html` badges and card pages.
- **Grade → badge color** (applies to both the index and card pages):
  - ≥ 9: `bg-success`
  - 8 – 8.9: `bg-warning text-dark`
  - < 8: `bg-secondary`
  - The condition progress bar uses the same buckets; bar width is `nota × 10` percent.
- **Filenames** in `pages/` are descriptive kebab-case, typically `<pokemon>-<set>-<grader>-<grade>.html`. Match the slug used by the `onclick` in `index.html`.
- **Dates** are always `DD/MM/YYYY` in card content.
- **Graders supported** (each has its own cert URL pattern — see existing pages for examples): GBA, Manafix/MGS, CAPY, CGC, ACE, BGS, PSA, BRG, RPA, ARS, TAG.
- **Indentation**: 4 spaces in `template_pericia.html` and most card pages; 2 spaces in `index.html`. Match the file you are editing.

## Gotchas

- `pages/sabrinasgaze-psa-trainer1999.html.backup` is a leftover backup file; ignore unless asked to clean up.
- There is no automated check that an entry in `index.html` has a matching file in `pages/` (or vice versa); verify both sides exist after edits.

## AIOX framework (installed, mostly inert)

The `aiox-core@5.2.x` framework was installed via `npx aiox-core install --merge`. It dropped ~34 MB of agent/workflow scaffolding into `.aiox-core/` and `.claude/` (agents/, rules/, hooks/, commands/). **This project is still a static HTML site — there is no Node app to lint, test, or build**, so most of AIOX's playbook (story-driven dev, `npm run lint`, `npm test`, `docs/stories/`, push gates) does not apply here.

What *is* usable:
- **Agent activation** via `@<name>` (and `*<command>` for agent commands). Useful ones for this repo: `@analyst` for card research, `@ux-design-expert` for layout tweaks, `@qa` for accessibility/HTML review. Ignore `@dev`, `@sm`, `@po`, `@architect` for now — they assume a Node codebase with stories.
- **Skills added by AIOX** — `tech-search`, `architect-first`, `checklist-runner`, `mcp-builder`, `synapse`, `skill-creator`. The project's own skills (`pericia-template`, `acessibilidade`, `bootstrap-guidelines`, `codigo-html`, `estrutura-paginas`) remain the primary ones for authoring new card pages.
- **`.claude/rules/`** — auto-loaded contextual rules; harmless when not actively building Node code.

Active hooks (in `.claude/settings.local.json`, gitignored):
- `PreToolUse` on Bash → `enforce-git-push-authority.cjs` (blocks unauthorized `git push`)
- `UserPromptSubmit` → `synapse-engine.cjs` (context engine; adds latency to every prompt)

If you want to fully remove AIOX, run: `Remove-Item -Recurse -Force .aiox-core, .claude/agents, .claude/rules, .claude/hooks, .claude/commands, .claude/settings.local.json, .claude/skills/AIOX, .claude/skills/architect-first, .claude/skills/checklist-runner, .claude/skills/coderabbit-review, .claude/skills/mcp-builder, .claude/skills/skill-creator, .claude/skills/synapse, .claude/skills/tech-search` (verify the list against current state first).
