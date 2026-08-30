# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

This project is a dynamic web application built with **FastAPI**, **MongoDB**, and **Jinja2** templates, serving a portfolio of graded Pokémon TCG cards.

**(Note: This project recently migrated from a static HTML GitHub Pages architecture. The old static generation script, Cloudinary integration, and `pages/` directory have been removed in favor of this dynamic stack.)**

## Architecture

- **Backend Framework**: FastAPI (`backend/main.py`).
- **Templating**: Jinja2 (`backend/templates/`). HTML pages are rendered dynamically.
- **Database**: MongoDB (`backend/database.py` and `backend/models.py`). Cards are queried and injected into the HTML templates.
- **Storage**: Cloudinary SDK (`backend/storage.py`). Handled via FastAPI upload endpoint `/api/upload`.
- **Authentication**: Session-based auth with bcrypt hashed password. Users are stored in `users` collection and active sessions in `sessions`. Default user is `afonsolelis` (pwd seeded on startup).

## Development Guidelines

- **Working Directory**: All active code is now under the `backend/` directory. If you are asked to edit the layout or logic, you should look into `backend/templates/`, `backend/static/`, and `backend/main.py`.
- **Authentication**: Modification routes (POST, PUT, DELETE) and `/admin` require session-cookie authentication. Read routes (`/`, `/laudo/{id}`) are public.
- **Adding new cards**: Read `.claude/skills/pericia-template/SKILL.md`, which routes to the canonical `.agents/skills/adicionar-carta/SKILL.md`. Card data is validated and inserted into MongoDB and local images are uploaded to Cloudinary. Never write a hard-coded HTML page for a card.
- **Layout Adjustments**: When editing the visual representation of a card, edit `backend/templates/laudo.html` or `backend/templates/index.html`. Remember to use Jinja2 templating syntax `{{ var }}` for dynamic text.
- **Environment**: You must set environment variables (or rely on a `.env` file) for database connections and Cloudinary if you need to run the application to test features.
