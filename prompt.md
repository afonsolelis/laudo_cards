# laudo_cards — Handoff / Resume Prompt

> Read this first after restarting Claude Code. It captures where we left off so we can continue without re-deriving everything.

## Context
`laudo_cards` is a FastAPI + MongoDB + Jinja2 app (a graded Pokémon TCG card portfolio), deployed on **Railway** (project `laudo-cards`, env `production`). Code lives under `backend/`. The site is live at **https://laudocards-production.up.railway.app**.

The goal of this session was to **cut Railway costs**. Investigation showed the cost driver was **always-on compute** (4 services running 24/7: app, MongoDB, MinIO `Bucket`, MinIO `Console`), **not** volume storage (all volumes combined were ~1.2 GB — pennies). Decision: **drop MinIO entirely and move media to Cloudinary.**

## What's already done ✅
1. **Media migrated MinIO → Cloudinary** (commit `b5cf878`, pushed to `main`, deployed SUCCESS):
   - `backend/storage.py` — now uses the Cloudinary SDK; `upload_file_to_cloudinary()` runs the upload in a threadpool. Returns `secure_url`.
   - `backend/main.py` — `/api/upload` calls Cloudinary; same response contract `{"url": ...}`, so the admin form + `index`/`laudo` templates were untouched.
   - `requirements.txt` (root + `backend/`) — `boto3` → `cloudinary`.
2. **Cloudinary env vars set on Railway** (`laudo_cards` service): `CLOUDINARY_CLOUD_NAME` (`dyhjjms8y`), `CLOUDINARY_API_KEY`, `CLOUDINARY_API_SECRET`, `CLOUDINARY_FOLDER` (`laudo_cards`).
3. **Local `.env` created** at repo root (gitignored) with the Cloudinary creds + `DB_NAME` + `MONGO_URL` (defaults to localhost).
4. **MinIO + all volumes deleted** by the user (MinIO `Bucket`, `Console`, plus 6 orphaned volumes: postgres ×2, docmost ×2, redis, valkey).
5. **MongoDB wiped clean** — `cards` and `graders` collections both at 0 docs. Fresh start (project is not really in production yet).
6. **Claude permission mode set to `bypassPermissions`** in `.claude/settings.local.json` (takes effect on restart).

## Current state
- Services remaining on Railway: `laudo_cards` (app) + `MongoDB`. MinIO is gone.
- DB is empty. New card uploads will go to Cloudinary.
- App boots cleanly (Cloudinary config runs at import; verified HTTP 200 on home).

## Open items / next steps 🔜
- [ ] **Verify an end-to-end upload** via `/admin` actually lands in Cloudinary and renders on a card page.
- [ ] **Remove dead `MINIO_*` env vars** from the `laudo_cards` service (`MINIO_ENDPOINT`, `MINIO_ACCESS_KEY`, `MINIO_SECRET_KEY`, `MINIO_BUCKET`) — app no longer reads them. Left in place to avoid an extra redeploy.
- [ ] **MongoDB egress**: `MONGO_URL` uses the public proxy (`*.proxy.rlwy.net`) instead of the private `mongo.railway.internal` domain — switching cuts egress cost.
- [ ] Delete leftover scratch file `_verify_wipe_db.py` if still present (gitignored; deletion was pending when we paused).
- [ ] Start adding cards fresh via `/admin`.

## Handy references
- Railway project id: `bc62d449-6fdb-4347-b8c8-7a309f8401ba` · env `production`: `04dbf104-f939-4ff6-b176-0fb71b10aa7f` · `laudo_cards` service: `4d50ab7e-5aa9-4095-a311-e891a5689177`
- CLI: `railway link --project laudo-cards`, `railway variables --service laudo_cards --kv`, `railway logs`.
- Secrets live in the local `.env` and in Railway service vars — **not** in this file.
- DB wipe was done with a throwaway pymongo script reading `MONGO_URL`/`DB_NAME` from env.
