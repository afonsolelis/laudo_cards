# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A portfolio of graded Pokémon TCG cards: a **static site** (`site/`) deployed to **GitHub Pages** that talks directly to **Supabase** (Postgres with RLS, Auth and Storage).

The old FastAPI + MongoDB + Railway backend has been removed. Don't bring it back.

## Architecture

- **Pages**: `site/index.html` (gallery), `site/laudo.html?id=…` (card report), `site/admin.html` (CRUD), `site/login.html`. `site/404.html` redirects old `/laudo/<id>` links.
- **Client**: `site/js/supabase.js` (shared client, publishable key) and `site/js/common.js` (escaping and formatting helpers).
- **Database**: `supabase/schema.sql` (idempotent): tables `admins`, `graders`, `cards`; public read, writes only for emails listed in `admins`; `card-images` bucket.
- **Graders**: ARS, GBA, PSA and GRADD (seeded in `schema.sql`). The home page builds one filter button per grader, in `created_at` order. `cards.grading_company` is a FK to `graders.name`.
- **Reset**: `supabase/reset.sql` wipes every card and recreates the graders (destructive).
- **Deploy**: `.github/workflows/pages.yml` publishes `site/` on every push to `main` that touches `site/**`.

## Guidelines

- Escape every value that comes from the database with `escapeHtml`, and pass URLs through `safeUrl`.
- After changing `site/css/styles.css`, bump `?v=` in every page.
- Schema changes go in `supabase/schema.sql` and must stay idempotent.
