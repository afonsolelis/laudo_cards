-- Laudo Cards — zera o acervo e recria as graduadoras.
-- DESTRUTIVO: apaga todas as cartas, todas as graduadoras e todas as imagens
-- do bucket card-images. Rode no SQL Editor do Supabase depois de schema.sql.

begin;

delete from public.cards;
delete from public.graders;

insert into public.graders (name, created_at) values
  ('ARS',   now()),
  ('GBA',   now() + interval '1 second'),
  ('PSA',   now() + interval '2 seconds'),
  ('GRADD', now() + interval '3 seconds');

commit;

-- O Supabase bloqueia DELETE direto em storage.objects. Para limpar as imagens,
-- esvazie o bucket card-images pelo painel (Storage → card-images → Empty bucket).
