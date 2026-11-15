# Laudo Cards 🎴

Portfólio digital de cartas Pokémon TCG graduadas: galeria pública, laudo por carta (subgrades, certificado, links de mercado) e painel administrativo.

## Stack

- **Site estático** (`site/`): HTML, Bootstrap 5.3 e JavaScript em módulos, publicado no **GitHub Pages**.
- **Supabase**: Postgres com RLS (leitura pública, escrita só para administradores), Auth (login do admin) e Storage (bucket `card-images`).

## Graduadoras

ARS · GBA · PSA · GRADD. Na home, cada graduadora vira um botão de filtro com a contagem de cartas. Para incluir outra, cadastre pelo painel admin.

## Configuração do Supabase

1. No SQL Editor, rode `supabase/schema.sql` (idempotente).
2. Em *Authentication → Sign In / Providers*, desative "Allow new users to sign up".
3. Para zerar o acervo, rode `supabase/reset.sql` e esvazie o bucket `card-images` em *Storage*.

## Rodando localmente

```bash
python3 -m http.server -d site 8000
```

Acesse `http://localhost:8000`. O site usa o projeto Supabase configurado em `site/js/supabase.js`.

## Estrutura

```text
site/
├── index.html      # Galeria com busca, filtro por graduadora e ordenação por nota
├── laudo.html      # Laudo individual (?id=)
├── admin.html      # CRUD de cartas e graduadoras
├── login.html
├── 404.html        # Redireciona links antigos /laudo/<id>
├── css/styles.css
└── js/             # Cliente Supabase e helpers
supabase/
├── schema.sql      # Tabelas, RLS, bucket e graduadoras
└── reset.sql       # Zera cartas e recria graduadoras
```
