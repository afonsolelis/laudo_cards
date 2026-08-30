---
name: estrutura-paginas
description: Mantém a estrutura visual dinâmica da galeria e dos laudos do Laudo Cards. Use ao alterar layout, seções ou apresentação em backend/templates/index.html e backend/templates/laudo.html; não use para cadastrar uma carta.
---

# Estrutura visual dinâmica

O projeto usa FastAPI, MongoDB e Jinja2. Todas as cartas compartilham os mesmos
templates; não existem páginas HTML individuais por carta.

## Limite desta skill

- Para adicionar uma carta, use `pericia-template`, que encaminha para a skill
  canônica `.agents/skills/adicionar-carta/SKILL.md`.
- Para alterar a galeria, edite `backend/templates/index.html`.
- Para alterar o laudo individual, edite `backend/templates/laudo.html`.
- Para alterar o cadastro administrativo, edite
  `backend/templates/admin.html` e confirme o contrato em `backend/models.py`.

Uma alteração visual deve funcionar para todos os documentos válidos, inclusive
campos opcionais ausentes e registros antigos.

## Estrutura atual

### Galeria (`index.html`)

- Navegação e acesso ao painel administrativo
- Hero com total de cartas e graduadoras
- Busca, filtro por graduadora, ordenação por nota e filtro de troca
- Grid de cards com imagem frontal, identificação, raridade, nota e graduadora
- Toggle de disponibilidade para usuários autenticados
- Footer

### Laudo (`laudo.html`)

- Navegação e cabeçalho com nome completo e certificado
- Fotos de frente e verso com ampliação em modal
- Identificação da carta
- Dados de aquisição exibidos somente ao usuário autenticado
- Graduação, certificado e link oficial condicional
- Links externos condicionais
- Nota final e subgrades condicionais
- Observações técnicas e histórico condicionais
- Acesso de edição somente ao usuário autenticado

## Regras

- Preserve a sintaxe Jinja2 e acesse somente campos existentes em
  `backend/models.py` ou documentos legados tratados explicitamente.
- Proteja campos opcionais com condicionais; não renderize botões vazios,
  imagens quebradas ou blocos sem conteúdo.
- Não exponha `acquisition_price`, controles administrativos ou ações de escrita
  a visitantes anônimos.
- Mantenha links externos com `target="_blank"` e
  `rel="noopener noreferrer"`.
- Mantenha textos alternativos significativos, navegação por teclado e rótulos
  acessíveis.
- Reuse os tokens e componentes de `backend/static/css/styles.css`; não recoloque
  o visual estático antigo.
- Mudanças no schema exigem atualização coordenada do modelo, formulário,
  payload JavaScript, templates, testes e da referência da skill de cadastro.

## Verificação

Ao concluir uma mudança visual:

1. Execute os testes do backend.
2. Renderize uma carta completa e uma carta com campos opcionais ausentes.
3. Verifique galeria e laudo em viewport móvel e desktop.
4. Confirme que a inclusão de cartas continua sendo feita somente no MongoDB.
