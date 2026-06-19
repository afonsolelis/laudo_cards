# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

This project is a dynamic web application built with **FastAPI**, **MongoDB**, and **Jinja2** templates, serving a portfolio of graded Pokémon TCG cards.

**(Note: This project recently migrated from a static HTML GitHub Pages architecture. The old static generation script, Cloudinary integration, and `pages/` directory have been removed in favor of this dynamic stack.)**

## Architecture

- **Backend Framework**: FastAPI (`backend/main.py`).
- **Templating**: Jinja2 (`backend/templates/`). HTML pages are rendered dynamically.
- **Database**: MongoDB (`backend/database.py` and `backend/models.py`). Cards are queried and injected into the HTML templates.
- **Storage**: MinIO / S3 compatible (`backend/storage.py`). Handled directly by FastAPI upload routes.
- **Frontend Styles**: Bootstrap 5.3 via CDN + `backend/static/css/styles.css`.

## Development Guidelines

- **Working Directory**: All active code is now under the `backend/` directory. If you are asked to edit the layout or logic, you should look into `backend/templates/`, `backend/static/`, and `backend/main.py`.
- **Adding new cards**: The system relies on adding card data to the MongoDB collection (`cards_collection`) and uploading their respective images to MinIO. We no longer write hard-coded HTML pages.
- **Layout Adjustments**: When editing the visual representation of a card, edit `backend/templates/laudo.html` or `backend/templates/index.html`. Remember to use Jinja2 templating syntax `{{ var }}` for dynamic text.
- **Environment**: You must set environment variables (or rely on a `.env` file) for database connections and MinIO if you need to run the application to test features.
