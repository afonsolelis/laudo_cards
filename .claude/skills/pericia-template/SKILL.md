---
name: pericia-template
description: Cadastra novas cartas graduadas no Laudo Cards atual. Use quando o usuário pedir para criar um laudo ou adicionar, cadastrar ou incluir uma carta no acervo MongoDB.
---

# Cadastro de cartas na aplicação atual

O fluxo antigo de gerar `pages/*.html` foi descontinuado. Antes de cadastrar uma
carta, leia e siga integralmente a skill canônica em:

`../../../.agents/skills/adicionar-carta/SKILL.md`

Resolva as referências e scripts a partir do diretório da skill canônica. Não
crie páginas HTML individuais: a aplicação FastAPI renderiza os cards e laudos
dinamicamente com dados do MongoDB.
