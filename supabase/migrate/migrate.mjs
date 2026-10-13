// Migra o acervo do MongoDB (Railway) para o Postgres do Supabase.
//
// Uso (a partir da raiz do repo, com MONGO_URL, DB_NAME e PG_URL no ambiente):
//   npm --prefix supabase/migrate install
//   node --env-file=.env supabase/migrate/migrate.mjs            # simulação
//   node --env-file=.env supabase/migrate/migrate.mjs --apply    # grava
//
// Idempotente: aplica supabase/schema.sql e faz upsert pelo ObjectId, então
// pode ser rodado de novo sem duplicar cartas.

import fs from 'node:fs';
import { createRequire } from 'node:module';

const require = createRequire(import.meta.url);
const { MongoClient } = require('mongodb');
const pg = require('pg');

const APPLY = process.argv.includes('--apply');
const { MONGO_URL, DB_NAME = 'laudo_cards', PG_URL } = process.env;
if (!MONGO_URL || !PG_URL) {
  console.error('Defina MONGO_URL e PG_URL (e opcionalmente DB_NAME).');
  process.exit(1);
}

const schemaSql = fs.readFileSync(new URL('../schema.sql', import.meta.url), 'utf8');

const num = (v) => (v === null || v === undefined || v === '' ? null : Number(v));
const str = (v) => (v === null || v === undefined || v === '' ? null : String(v));

function toDate(value, fallback) {
  if (typeof value === 'string' && /^\d{4}-\d{2}-\d{2}$/.test(value)) return value;
  if (value instanceof Date) return value.toISOString().slice(0, 10);
  return fallback.toISOString().slice(0, 10);
}

function toRow(doc) {
  const createdAt = doc._id.getTimestamp();
  const grade = doc.grade || {};
  const links = doc.links || {};
  return {
    id: doc._id.toHexString(),
    name: doc.name,
    number: String(doc.number ?? ''),
    full_name: doc.full_name || doc.name,
    set_name: doc.set_name,
    year: num(doc.year),
    rarity: doc.rarity,
    pokemon_type: doc.pokemon_type,
    language: doc.language,
    illustrator_name: doc.illustrator_name,
    acquisition_price: num(doc.acquisition_price),
    added_date: toDate(doc.added_date, createdAt),
    available_for_trade: Boolean(doc.available_for_trade),
    grading_company: doc.grading_company,
    certificate_number: String(doc.certificate_number ?? ''),
    grading_year: num(doc.grading_year),
    cert_link: str(doc.cert_link),
    image_front_url: str(doc.image_front_url),
    image_back_url: str(doc.image_back_url),
    grade: {
      final: num(grade.final),
      description: grade.description ?? '',
      centering: num(grade.centering),
      corners: num(grade.corners),
      edges: num(grade.edges),
      surface: num(grade.surface),
    },
    links: {
      tcg_player: str(links.tcg_player),
      price_charting: str(links.price_charting),
      liga_pokemon: str(links.liga_pokemon),
      myp_cards: str(links.myp_cards),
      ebay: str(links.ebay),
    },
    history_markdown: str(doc.history_markdown),
    grader_notes_markdown: str(doc.grader_notes_markdown),
    card_history: str(doc.card_history),
    created_at: createdAt.toISOString(),
  };
}

const mongo = new MongoClient(MONGO_URL);
await mongo.connect();
const db = mongo.db(DB_NAME);
const graders = await db.collection('graders').find().toArray();
const cards = await db.collection('cards').find().sort({ _id: 1 }).toArray();
await mongo.close();

const graderNames = new Set(graders.map((g) => g.name));
const missing = [...new Set(cards.map((c) => c.grading_company))].filter((n) => !graderNames.has(n));
const rows = cards.map(toRow);

console.log(`Mongo: ${graders.length} graduadoras, ${cards.length} cartas.`);
if (missing.length) console.log(`Graduadoras usadas por cartas mas ausentes (serão criadas): ${missing.join(', ')}`);
for (const r of rows) {
  const problems = ['name', 'set_name', 'year', 'rarity', 'grading_year']
    .filter((k) => r[k] === null || r[k] === undefined || Number.isNaN(r[k]));
  if (r.grade.final === null || Number.isNaN(r.grade.final)) problems.push('grade.final');
  if (problems.length) console.log(`  ⚠ ${r.id} (${r.name}): campos inválidos ${problems.join(', ')}`);
}

if (!APPLY) {
  console.log('\nSimulação concluída. Rode com --apply para gravar no Supabase.');
  process.exit(0);
}

const client = new pg.Client({ connectionString: PG_URL });
await client.connect();
try {
  await client.query(schemaSql);
  await client.query('begin');
  for (const name of [...graderNames, ...missing]) {
    await client.query('insert into public.graders (name) values ($1) on conflict (name) do nothing', [name]);
  }
  const cols = Object.keys(rows[0] ?? {});
  for (const r of rows) {
    const values = cols.map((c) => (c === 'grade' || c === 'links' ? JSON.stringify(r[c]) : r[c]));
    await client.query(
      `insert into public.cards (${cols.join(', ')})
       values (${cols.map((_, i) => `$${i + 1}`).join(', ')})
       on conflict (id) do update set ${cols.filter((c) => c !== 'id').map((c) => `${c} = excluded.${c}`).join(', ')}`,
      values,
    );
  }
  await client.query('commit');
  const { rows: [count] } = await client.query(
    'select (select count(*) from public.graders) graders, (select count(*) from public.cards) cards',
  );
  console.log(`Supabase: ${count.graders} graduadoras, ${count.cards} cartas.`);
} catch (err) {
  await client.query('rollback').catch(() => {});
  throw err;
} finally {
  await client.end();
}
