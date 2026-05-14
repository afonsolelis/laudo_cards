---
name: pericia-template
description: Cria novas páginas de perícia de cartas Pokémon TCG graduadas usando o template padronizado. Use quando o usuário pedir para criar uma nova perícia, laudo de carta, ou adicionar uma nova carta ao portfólio.
---

# Skill: Criador de Páginas de Perícia

Esta skill automatiza a criação de páginas de perícia de cartas Pokémon TCG graduadas, usando o template padronizado do projeto.

## Quando Usar

- Quando o usuário pedir para criar uma nova perícia
- Quando quiser adicionar uma nova carta ao portfólio
- Quando precisar documentar uma carta graduada
- Quando mencionar "nova perícia", "criar laudo", "adicionar carta"

## Processo de Criação

### 1. Coleta de Informações

Faça perguntas ao usuário usando o **AskUserQuestion** tool para coletar:

**Informações Básicas:**
- Nome da carta
- Número da carta
- Coleção/Set
- Ano de lançamento
- Raridade (use a padronização abaixo)
- Tipo do Pokémon
- Idioma
- Fabricante
- Ilustrador/Artista
- URLs das fotos (frente e verso)

**Padronização de Raridades:**
Use sempre o formato misto português/inglês com abreviações padronizadas:
- SAR: "Ilustração Especial Rara (SAR)"
- AR: "Ilustração Rara (AR)"
- HR: "Hyper Rare (HR)"
- SR: "Shiny Rare (SR)"
- UR: "Ultra Rare (UR)"
- C: "Comum (C)"

**Padronização de Tipo (PT puro + qualifier opcional):**
- Pokémon types em português: `Elétrico`, `Fogo`, `Água`, `Lutador`, `Psíquico`, `Planta`, `Sombrio`, `Metal`, `Incolor`, `Dragão`, `Férea`
- Se houver qualifier (Terastal, TAG TEAM, VSTAR), use entre parênteses: `Elétrico (Terastal)`, `Psíquico (TAG TEAM GX)`
- Para cartas Treinador: `Treinador — Apoiador`, `Treinador — Item`, etc.

**Padronização de Idioma (apenas estes 6 valores):**
`Português`, `Japonês`, `Inglês`, `Chinês Simplificado`, `Chinês Tradicional`, `Coreano`

**Padronização de Fabricante:**
- `The Pokémon Company / Copag` — Brasil (produto da Copag)
- `The Pokémon Company` — internacional moderno (2003+)
- `Wizards of the Coast` — legado 1996-2003 (Base Set, Jungle, etc)
- `Topsun` — cartas Topsun vintage 1995-1997

**Informações de Graduação:**
- Graduadora (GBA, Manafix, CAPY, CGC, ACE, BGS, PSA, BRG, RPA, ARS, TAG, Gradd)
- Certificado
- Nota final
- Descrição da nota (Mint, Heavy Played, etc)
- **Label fixo:** "Data da Certificação" (não use "Data da Avaliação")
- Notas por componente:
  - Centering
  - Corners
  - Edges
  - Surface
- Ranking/População (mesma nota, nota maior, total)

**Informações Adicionais:**
- Links de referência (MyP, TCGPlayer, Liga Pokémon, Price Charting, etc)
- Campos opcionais (Edição, Versão, Lançamento, Registro AAA)

### 2. Decisões de Estrutura

**Estrutura de Links (DEFAULT: Opção B — seção separada):**
- O template já vem com a seção "Links de Referência e Consulta de Preços" como padrão canônico (card dedicado com grid 2x2 de botões `btn-outline-dark`).
- Se a carta NÃO tiver links externos (apenas o laudo oficial da graduadora), **remova a seção inteira** — o card de Graduação já contém o botão "Ver Laudo Oficial".
- NÃO use o padrão antigo de botões empilhados dentro do card de Graduação.

**Campos Adicionais opcionais:**
- Incluir campo "Edição"? (cartas com edição diferenciada como Mew Ancião)
- Incluir campo "Versão"? (variantes promocionais)
- Incluir campo "Lançamento"? (data específica de lançamento mês/ano)
- Incluir campo "Registro AAA"? (apenas GBA)

**Observações:**
- Incluir nota sobre alteração de dados ao longo do tempo? (recomendado para certificações recentes)

**Footer:**
- Formato padrão: "Laudo gerado para: [CERTIFICADO]"

### 3. Conteúdo Dinâmico

Solicite ao usuário:

**Observações Técnicas Detalhadas:**
Para cada componente (Centering, Corners, Edges, Surface):
- Descrição detalhada da condição
- Ícone apropriado (✓ positivo, ⚠ neutro, ! atenção)
- Cor do texto (success, secondary, warning)

**Observação de Autenticidade:**
- Descrição da verificação de autenticidade

**Histórico de Proveniência:**
- Número de itens na timeline
- Para cada item:
  - Data/período
  - Título do evento
  - Descrição completa
  - Se deve iniciar expandido (collapse show)

**Informações sobre Artista/Ilustrador:**
- Breve descrição
- Lista de características/trabalhos

**Notas sobre Graduadora:**
- Informações relevantes sobre a graduadora

### 4. Geração do Arquivo

1. Leia o template: `template_pericia.html`
2. Substitua todas as variáveis `{{VARIAVEL}}` pelos valores coletados
3. Ajuste seções opcionais conforme as escolhas do usuário
4. Gere o conteúdo dinâmico (observações, histórico, informações de artista)
5. Salve em `pages/[nome-arquivo].html`

### 5. Cores de Badge Automáticas

**Por Nota:**
- 10 ou 9.5+: `bg-success` (verde)
- 9 - 9.25: `bg-success` (verde)
- 8 - 8.5: `bg-warning text-dark` (amarelo)
- 6 - 7.5: `bg-secondary` (cinza)
- 3 - 5.5: `bg-secondary` (cinza)

**Barra de Progresso:**
- Nota 9-10: `bg-success`
- Nota 8-8.9: `bg-warning`
- Nota <8: `bg-secondary`

**Porcentagem da Barra:**
- Calcular: `nota × 10` (ex: nota 9 = 90%)

### 6. Design System (use SEMPRE)

**Utility classes (em `css/styles.css`)** — use ao invés de inline styles:
- `.photo-thumb` — foto clicável 400px com cursor pointer
- `.fs-strong` — texto destacado (1.1rem)
- `.fs-label` — texto de label (0.95rem)
- `.fs-figure` — número em destaque (1.5rem)
- `.fs-small-label` — label pequeno (0.9rem)
- `.col-label` — coluna de label em tabela (40%)
- `.progress-tall` — barra de progresso alta (25px)
- `.progress-thin` — barra de progresso fina (8px)
- `.pricechart-frame` — iframe PriceCharting (min-height 600px)
- `.badge-ancien` / `.alert-ancien` — cores temáticas Ancião

**NÃO use `style="font-size: 1.1rem;"`** ou similares — use as classes acima.

**H1 fixo:** `<h1 class="h3 mb-2">Descritivo Técnico</h1>` (não use "Documentação Técnica" ou variantes)

**Card-header colors (regra):**
- `bg-dark text-white` — seções principais (Graduação, Histórico de Proveniência)
- `bg-secondary text-white` — seções auxiliares (Fotos, Identificação, Análise, Links de Referência)

### 7. Validação Final

Antes de salvar, verifique:
- ✅ Todas as variáveis `{{...}}` foram substituídas
- ✅ URLs das fotos estão corretas
- ✅ Links externos estão completos
- ✅ Accordion do histórico tem IDs únicos (collapse1, collapse2, etc)
- ✅ Primeiro item do histórico tem `collapse show` se apropriado
- ✅ Cores dos badges correspondem às notas
- ✅ Raridade usa o formato padronizado (SAR, AR, HR, SR, UR, C)
- ✅ Tipo usa formato PT puro + qualifier opcional
- ✅ Idioma é um dos 6 valores canônicos
- ✅ Fabricante é um dos 4 canônicos
- ✅ Data label é "Data da Certificação"
- ✅ H1 é "Descritivo Técnico"
- ✅ Header histórico é "Histórico de Proveniência"
- ✅ Nome do arquivo usa formato kebab-case (ex: pikachu-gold.html)
- ✅ `<a target="_blank">` tem `rel="noopener noreferrer"`
- ✅ Tags Bootstrap CDN têm SRI integrity hash
- ✅ Inline styles substituídos por utility classes do design system

## Referências

Para detalhes completos sobre variáveis e estrutura, consulte [reference.md](reference.md).

## Exemplo de Fluxo

```
Usuário: "Criar perícia para o Charizard ex"

Assistente:
1. Fazer perguntas para coletar informações básicas
2. Perguntar sobre preferências de estrutura
3. Solicitar observações técnicas e histórico
4. Gerar HTML com base no template
5. Salvar em pages/charizard-ex.html
6. Informar ao usuário que a página foi criada
```

## Notas Importantes

- **Consistência:** Mantenha o padrão das páginas existentes
- **Formato de Data:** Sempre DD/MM/YYYY
- **Nome de Arquivo:** Use kebab-case e seja descritivo
- **Graduadoras:** Respeite as diferenças entre Manafix, GBA, CAPY, CGC, ACE, BGS e PSA
- **Bootstrap 5.3.0:** Use as classes corretas do Bootstrap
- **Accordion IDs:** Devem ser únicos dentro da página
- **Raridades:** SEMPRE use o formato padronizado misto (português + abreviação inglesa)
