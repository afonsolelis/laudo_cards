-- Laudo Cards — schema do Supabase (Postgres + Storage).
-- Idempotente: pode ser executado mais de uma vez.
--
-- Leitura é pública (anon). Escrita só para usuários autenticados cujo e-mail
-- esteja em public.admins. Desative "Allow new users to sign up" em
-- Authentication → Sign In / Providers para que ninguém mais crie conta.

create extension if not exists pgcrypto;

-- Administradores ------------------------------------------------------------

create table if not exists public.admins (
  email text primary key check (email = lower(email))
);

insert into public.admins (email) values ('afonsolelis@gmail.com')
on conflict do nothing;

create or replace function public.is_admin()
returns boolean
language sql
stable
security definer
set search_path = public
as $$
  select exists (
    select 1 from public.admins
    where email = lower(coalesce(auth.jwt() ->> 'email', ''))
  );
$$;

-- Graduadoras ----------------------------------------------------------------

create table if not exists public.graders (
  id uuid primary key default gen_random_uuid(),
  name text not null unique check (length(trim(name)) > 0),
  created_at timestamptz not null default now()
);

-- Cartas ---------------------------------------------------------------------

create table if not exists public.cards (
  -- Texto para preservar os ObjectIds do Mongo (links /laudo/<id> antigos).
  id text primary key default replace(gen_random_uuid()::text, '-', ''),

  name text not null,
  number text not null,
  full_name text not null,
  set_name text not null,
  year int not null,
  rarity text not null,
  pokemon_type text not null,
  language text not null,
  illustrator_name text not null,

  acquisition_price numeric(12, 2) check (acquisition_price >= 0),
  added_date date default current_date,
  available_for_trade boolean not null default false,

  -- A FK substitui a validação feita em Python: uma graduadora inexistente
  -- é rejeitada, e renomear a graduadora atualiza as cartas.
  grading_company text not null
    references public.graders (name) on update cascade on delete restrict,
  certificate_number text not null,
  grading_year int not null,
  cert_link text,

  image_front_url text,
  image_back_url text,

  -- { final, description, centering?, corners?, edges?, surface? }
  grade jsonb not null check (
    jsonb_typeof(grade -> 'final') = 'number'
    and jsonb_typeof(grade -> 'description') = 'string'
  ),
  -- { tcg_player?, price_charting?, liga_pokemon?, myp_cards?, ebay? }
  links jsonb not null default '{}'::jsonb,

  history_markdown text,
  grader_notes_markdown text,
  card_history text,

  created_at timestamptz not null default now()
);

create index if not exists cards_created_at_idx on public.cards (created_at);

-- Permissões e RLS -----------------------------------------------------------

grant usage on schema public to anon, authenticated;
grant select on public.graders, public.cards to anon, authenticated;
grant insert, update, delete on public.graders, public.cards to authenticated;
revoke all on public.admins from anon, authenticated;

alter table public.admins enable row level security;
alter table public.graders enable row level security;
alter table public.cards enable row level security;

drop policy if exists "graders: leitura pública" on public.graders;
create policy "graders: leitura pública" on public.graders
  for select to anon, authenticated using (true);

drop policy if exists "graders: escrita admin" on public.graders;
create policy "graders: escrita admin" on public.graders
  for all to authenticated using (public.is_admin()) with check (public.is_admin());

drop policy if exists "cards: leitura pública" on public.cards;
create policy "cards: leitura pública" on public.cards
  for select to anon, authenticated using (true);

drop policy if exists "cards: escrita admin" on public.cards;
create policy "cards: escrita admin" on public.cards
  for all to authenticated using (public.is_admin()) with check (public.is_admin());

-- Storage: imagens das cartas ------------------------------------------------

insert into storage.buckets (id, name, public, file_size_limit, allowed_mime_types)
values ('card-images', 'card-images', true, 10485760,
        array['image/jpeg', 'image/png', 'image/webp', 'image/gif', 'image/heic'])
on conflict (id) do update set public = excluded.public,
  file_size_limit = excluded.file_size_limit,
  allowed_mime_types = excluded.allowed_mime_types;

drop policy if exists "card-images: escrita admin" on storage.objects;
create policy "card-images: escrita admin" on storage.objects
  for insert to authenticated
  with check (bucket_id = 'card-images' and public.is_admin());

drop policy if exists "card-images: alteração admin" on storage.objects;
create policy "card-images: alteração admin" on storage.objects
  for update to authenticated
  using (bucket_id = 'card-images' and public.is_admin());

drop policy if exists "card-images: remoção admin" on storage.objects;
create policy "card-images: remoção admin" on storage.objects
  for delete to authenticated
  using (bucket_id = 'card-images' and public.is_admin());
