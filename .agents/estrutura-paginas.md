# Estrutura de Páginas Individuais de Cartas

## Template Padrão

Toda página individual de carta deve seguir esta estrutura:

```
1. Navbar (igual em todas as páginas)
2. Container Principal
   2.1. Row com 2 colunas
       - Col-lg-5: Informações Básicas (card)
       - Col-lg-7: Perícia e Histórico (2 cards)
3. Botão de Voltar
4. Footer (igual em todas as páginas)
```

## Seção 1: Navbar

Deve ser idêntica em todas as páginas:
- Navbar dark com bg-dark
- Link de voltar para index.html
- Responsiva com toggler

## Seção 2: Informações Básicas (Coluna Esquerda)

**Card Header:**
- Cor de fundo relacionada ao tipo do Pokémon
- Emoji grande representando o tipo
- Nome do Pokémon

**Card Body:**
- Lista de informações básicas usando `list-group list-group-flush`
- Informações obrigatórias:
  - Nome
  - Número
  - Tipo (com badges)
  - Raridade
  - Set
  - HP
  - Artista

## Seção 3: Perícia Técnica (Coluna Direita - Primeiro Card)

**Card Header:** bg-primary

**Card Body contém:**

### 3.1. Ataques
- Cada ataque em um card separado com border colorida
- Informações:
  - Nome do ataque (com emoji)
  - Custo
  - Dano (se aplicável)
  - Descrição

### 3.2. Fraquezas e Resistências
- Row com 2 colunas
- Alerts coloridos:
  - Fraqueza: alert-info
  - Resistência: alert-success

### 3.3. Custo de Recuo
- Badge com número de energias

### 3.4. Avaliação da Condição
- Progress bar mostrando estado de conservação
- Lista de itens de checklist com checkmarks

## Seção 4: Histórico (Coluna Direita - Segundo Card)

**Card Header:** bg-success

**Card Body contém:**

### 4.1. Timeline em Accordion
- Cada evento histórico em um accordion-item
- Formato do título: "Data - Evento"
- Conteúdo: Descrição detalhada do evento
- Primeiro item aberto por padrão (collapse show)

### 4.2. Curiosidades
- Alert info no final
- Lista com fatos interessantes sobre a carta

## Seção 5: Botão de Voltar

```html
<div class="text-center mt-4">
    <a href="../index.html" class="btn btn-primary btn-lg">← Voltar à Coleção</a>
</div>
```

## Seção 6: Footer

Idêntico em todas as páginas:
- bg-dark text-white
- Copyright centralizado

## Exemplo de Eventos Históricos

Eventos típicos a incluir:
1. Lançamento inicial da carta
2. Aquisição (quando e como você obteve)
3. Avaliações profissionais
4. Mudanças de valor de mercado
5. Status atual

## Cores por Tipo de Pokémon

Sugestões de cores para card-header baseado no tipo:

- **Fogo**: bg-danger
- **Água**: bg-info ou bg-primary
- **Planta**: bg-success
- **Elétrico**: bg-warning text-dark
- **Psíquico**: bg-primary
- **Normal**: bg-secondary
- **Lutador**: bg-secondary
- **Dragão**: bg-primary
- **Fantasma**: bg-dark
- **Metálico**: bg-secondary

## Responsividade

- Mobile (<768px): Layout em coluna única
- Tablet (≥768px): Layout em coluna única
- Desktop (≥992px): Layout em 2 colunas (5-7)

Use: `col-lg-5` e `col-lg-7` para alcançar isso.

## Checklist de Qualidade

Antes de considerar uma página completa:

✅ Navbar funcional com link de voltar
✅ Informações básicas completas
✅ Pelo menos 2 ataques descritos
✅ Fraquezas e resistências definidas
✅ Progress bar de condição
✅ Pelo menos 3 eventos históricos
✅ Seção de curiosidades
✅ Botão de voltar
✅ Footer presente
✅ Responsivo em mobile
✅ Apenas classes Bootstrap (zero CSS customizado)
