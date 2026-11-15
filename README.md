# Laudo Cards 🎴

Portfólio digital de cartas Pokémon TCG graduadas: vitrine pública com cards por graduadora e um laudo por carta (fotos do slab, subgrades, certificado e links de mercado).

## Stack

Site 100% estático (`site/`): HTML, CSS e JavaScript em módulos, publicado no **GitHub Pages**. Sem backend nem banco: o acervo fica em `site/data/cards.json` e as imagens no Cloudinary.

## Graduadoras

A home mostra um card por graduadora. Só as listadas em `ACTIVE_GRADERS` (`site/js/common.js`) estão publicadas; as demais aparecem como "Em breve". Hoje: **GRADD**.

## Adicionar ou editar cartas

Edite `site/data/cards.json` e faça push para `main`. Cada carta precisa de um `id` único (usado em `laudo.html?id=`).

## Rodando localmente

```bash
python3 -m http.server -d site 8000
```

## Estrutura

```text
site/
├── index.html      # Home: hero, cards de graduadoras e grade de cartas
├── laudo.html      # Laudo individual (?id=)
├── 404.html        # Redireciona links antigos /laudo/<id>
├── data/cards.json # Acervo
├── css/styles.css
└── js/common.js    # Carregamento dos dados e helpers
```
