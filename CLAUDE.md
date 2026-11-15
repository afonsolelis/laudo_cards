# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A portfolio of graded Pokémon TCG cards: a **static site** (`site/`) deployed to **GitHub Pages**. There is no backend or database: the collection lives in `site/data/cards.json` and images are hosted on Cloudinary.

Supabase and the old FastAPI + MongoDB + Railway backend have both been removed. Don't bring them back.

## Architecture

- **Pages**: `site/index.html` (home: hero, one card per grader, grid of cards) and `site/laudo.html?id=…` (card report). `site/404.html` redirects old `/laudo/<id>` links.
- **Data**: `site/data/cards.json` (array of cards; `id` is unique and used in the URL).
- **Client**: `site/js/common.js` (`loadCards`, `ACTIVE_GRADERS`, escaping and formatting helpers).
- **Graders**: only graders in `ACTIVE_GRADERS` are published (currently GRADD); the others show as "Em breve".
- **Design**: light, clean, store-like (Botiga-inspired), Kumbh Sans, plain CSS without Bootstrap.
- **Deploy**: `.github/workflows/pages.yml` publishes `site/` on every push to `main` that touches `site/**`.

## Guidelines

- Escape every value that comes from `cards.json` with `escapeHtml`, and pass URLs through `safeUrl`.
- After changing `site/css/styles.css`, bump `?v=` in every page.
