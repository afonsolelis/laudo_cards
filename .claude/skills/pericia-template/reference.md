# Guia de Uso do Template de Perícia

## Análise das Diferenças entre as Páginas Existentes

### 1. **Mew Ancião (mew-anciao.html)**
- **Graduadora:** Manafix
- **Data:** "Data da Certificação"
- **Campos extras:** Edição, Versão
- **Artista:** "Artista" (não Ilustrador)
- **Histórico:** 8 itens de timeline (muito extenso)
- **Links:** Dentro da seção de graduação
- **Footer:** "Laudo gerado em: 19/12/2025"
- **Ranking:** Total (não População)

### 2. **Armarouge (armarouge.html)**
- **Graduadora:** GBA
- **Data:** "Data da Avaliação"
- **Campos extras:** Lançamento, Registro AAA
- **Artista:** "Ilustrador"
- **Histórico:** 4 itens de timeline
- **Links:** Dentro da seção de graduação
- **Footer:** "Laudo gerado em: 19/12/2025"
- **Ranking:** População

### 3. **Pikachu Gold (pikachu-gold.html)**
- **Graduadora:** GBA
- **Data:** "Programa" (Halloween GBA Promo 2025)
- **Campos extras:** Registro AAA
- **Artista:** "Ilustrador"
- **Histórico:** 2 itens de timeline
- **Links:** Seção separada com ícones Bootstrap
- **Footer:** "Laudo gerado para: P0000254"
- **Ranking:** População

---

## Variáveis do Template

### Variáveis Básicas

| Variável | Descrição | Exemplo |
|----------|-----------|---------|
| `{{NOME_CARTA}}` | Nome simples da carta | Pikachu ex |
| `{{NOME_CARTA_COMPLETO}}` | Nome completo com coleção | Pikachu ex - Prismatic Evolutions Hyper Rare |
| `{{NUMERO_CARTA}}` | Número da carta | 179/131 |
| `{{CERTIFICADO}}` | Número do certificado | P0000254 |

### Identificação da Carta

| Variável | Descrição | Exemplo |
|----------|-----------|---------|
| `{{COLECAO}}` | Nome da coleção | Prismatic Evolutions (Evoluções Prismáticas) |
| `{{ANO}}` | Ano de lançamento | 2025 |
| `{{RARIDADE}}` | Texto da raridade (use padronização) | Hyper Rare (HR) |
| `{{BADGE_COR_RARIDADE}}` | Classe CSS para cor do badge | bg-warning text-dark |
| `{{TIPO}}` | Tipo do Pokémon/carta | Pokémon ex Básico - Elétrico |
| `{{IDIOMA}}` | Idioma da carta | Português |
| `{{FABRICANTE}}` | Fabricante | The Pokémon Company International |
| `{{ARTISTA_LABEL}}` | Label do campo artista | Ilustrador / Artista |
| `{{ARTISTA_NOME}}` | Nome do artista | aky CG Works |

### Graduação

| Variável | Descrição | Exemplo |
|----------|-----------|---------|
| `{{GRADUADORA_NOME}}` | Sigla da graduadora | GBA |
| `{{GRADUADORA_NOME_COMPLETO}}` | Nome completo | GBA (Grupo Brasileiro de Autenticação) |
| `{{NOTA_FINAL}}` | Nota final | 9 |
| `{{NOTA_DESCRICAO}}` | Descrição da nota | Mint |
| `{{DATA_LABEL}}` | Label do campo de data | Data da Avaliação / Data da Certificação / Programa |
| `{{DATA_VALOR}}` | Valor da data/programa | 20/10/2025 / Halloween GBA Promo 2025 |

### Ranking de Graduação

| Variável | Descrição | Exemplo |
|----------|-----------|---------|
| `{{RANKING_MESMA_NOTA}}` | Quantidade com mesma nota | 0 |
| `{{RANKING_NOTA_MAIOR}}` | Quantidade com nota maior | 0 |
| `{{RANKING_TOTAL}}` | Total/População | 1 |
| `{{RANKING_TOTAL_LABEL}}` | Label do total | População / Total |

### Notas Detalhadas

| Variável | Descrição | Exemplo |
|----------|-----------|---------|
| `{{NOTA_CENTERING}}` | Nota de centralização | 9.25 |
| `{{NOTA_CORNERS}}` | Nota de cantos | 8.5 |
| `{{NOTA_EDGES}}` | Nota de bordas | 10 |
| `{{NOTA_SURFACE}}` | Nota de superfície | 10 |
| `{{BADGE_COR_CENTERING}}` | Cor do badge (bg-success, bg-warning, bg-secondary, bg-dark) | bg-success |
| `{{BADGE_COR_CORNERS}}` | Cor do badge | bg-warning text-dark |
| `{{BADGE_COR_EDGES}}` | Cor do badge | bg-success |
| `{{BADGE_COR_SURFACE}}` | Cor do badge | bg-success |

### Cores de Badge por Nota

- **10 ou 9.5+:** `bg-success` (verde)
- **9 - 9.25:** `bg-success` (verde)
- **8 - 8.5:** `bg-warning text-dark` (amarelo)
- **6 - 7.5:** `bg-secondary` (cinza)
- **3 - 5.5:** `bg-secondary` (cinza)

### Análise de Condição

| Variável | Descrição |
|----------|-----------|
| `{{DESCRICAO_ESCALA}}` | Descrição do sistema de graduação |
| `{{BADGE_COR_NOTA}}` | Cor do badge da nota geral |
| `{{PROGRESS_BAR_COR}}` | Cor da barra de progresso (bg-success, bg-warning, bg-secondary) |
| `{{PORCENTAGEM_NOTA}}` | Porcentagem para a barra (nota × 10) |
| `{{OBSERVACAO_CENTERING}}` | Texto de observação sobre centralização |
| `{{OBSERVACAO_AUTENTICIDADE}}` | Texto de observação sobre autenticidade |
| `{{REGISTRO_AAA_LABEL}}` | " (AAA)" se tiver registro, vazio caso contrário |

### Links de Referência

| Variável | Descrição |
|----------|-----------|
| `{{LINK_LAUDO_OFICIAL}}` | URL do laudo oficial da graduadora |
| `{{LINK_MYP}}` | URL da MyP Cards |
| `{{LINK_TCGPLAYER}}` | URL do TCGPlayer |
| `{{LINK_LIGA_POKEMON}}` | URL da Liga Pokémon |
| `{{LINK_PRICE_CHARTING}}` | URL do Price Charting |

### Histórico

| Variável | Descrição |
|----------|-----------|
| `{{TITULO_HISTORICO}}` | "Histórico de Proveniência" / "Histórico e Contexto" |
| `{{ARTISTA_DESCRICAO}}` | Breve descrição do artista |

### Fotos

| Variável | Descrição |
|----------|-----------|
| `{{URL_FOTO_FRENTE}}` | URL da foto da frente |
| `{{URL_FOTO_VERSO}}` | URL da foto do verso |

### Footer

| Variável | Descrição | Exemplo |
|----------|-----------|---------|
| `{{FOOTER_TEXTO}}` | Texto do rodapé | Laudo gerado em: 19/12/2025 / Laudo gerado para: P0000254 |

---

## Decisões de Design a Tomar

Ao criar uma nova perícia, você precisa decidir:

### 1. **Estrutura de Links**
- **Opção A:** Links dentro da seção de graduação (padrão Mew e Armarouge)
- **Opção B:** Seção separada "Links de Referência e Consulta de Preços" (padrão Pikachu)

No template, a Opção A está ativa e a Opção B está comentada. Descomente a seção desejada.

### 2. **Campos Adicionais de Identificação**
Decida quais campos incluir:
- Edição (Mew)
- Versão (Mew)
- Lançamento (Armarouge)
- Registro AAA (GBA)

Descomente as linhas apropriadas na tabela de identificação.

### 3. **Observação sobre Data da Perícia**
Incluir ou não a nota sobre alterações ao longo do tempo? (Mew e Armarouge têm, Pikachu não)

Descomente a seção se desejar incluir.

### 4. **Extensão do Histórico**
- Histórico curto (2-4 itens): Cartas modernas
- Histórico extenso (6-8 itens): Cartas vintage/históricas

### 5. **Footer**
Escolha o formato:
- "Laudo gerado em: [DATA]"
- "Laudo gerado para: [CERTIFICADO]"

---

## Checklist de Criação

- [ ] Coletar todas as informações da carta
- [ ] Escolher estrutura de links (A ou B)
- [ ] Definir campos adicionais necessários
- [ ] Preparar fotos (Cloudinary URLs)
- [ ] Escrever observações técnicas detalhadas
- [ ] Criar timeline do histórico
- [ ] Pesquisar informações sobre o artista/ilustrador
- [ ] Decidir sobre inclusão da observação de data
- [ ] Definir formato do footer
- [ ] Fazer busca e replace de todas as variáveis
- [ ] Revisar cores dos badges (notas altas = verde, médias = amarelo, baixas = cinza)
- [ ] Testar responsividade mobile
- [ ] Verificar todos os links externos

---

## Padrões de Consistência

### Cores de Badge por Graduadora

**Manafix:**
- Header: bg-dark
- Subheader: bg-secondary

**GBA:**
- Header: bg-dark
- Subheader: bg-secondary

### Notas de Condição

| Nota | Cor do Badge | Cor da Barra | Descrição |
|------|--------------|--------------|-----------|
| 10 | bg-success | bg-success | Gem Mint / Pristine |
| 9-9.5 | bg-dark ou bg-success | bg-success | Mint |
| 8-8.5 | bg-warning text-dark | bg-warning | Near Mint |
| 6-7 | bg-secondary | bg-secondary | Excellent / Moderately Played |
| 3-5 | bg-secondary | bg-secondary | Heavy Played / Damaged |

### Ícones para Observações

- ✓ `text-success` - Aspectos positivos
- ⚠ `text-secondary` - Aspectos neutros/moderados
- ! `text-warning` - Aspectos que precisam atenção

---

## Exemplo de Uso Rápido

```bash
# 1. Copiar template
cp template_pericia.html pages/nova-carta.html

# 2. Buscar e substituir todas as variáveis
# Use seu editor de código favorito (VS Code, Sublime, etc)
# Procure por {{NOME_CARTA}} e substitua por "Charizard ex"

# 3. Ajustar seções opcionais
# Comentar/descomentar conforme necessário

# 4. Preencher conteúdo dinâmico
# - Observações técnicas
# - Timeline do histórico
# - Informações do artista

# 5. Testar no navegador
```

---

## Padronização de Raridades

**IMPORTANTE:** Use sempre o formato misto português/inglês com abreviações padronizadas:

| Raridade | Formato Padrão | Cor do Badge |
|----------|----------------|--------------|
| Special Art Rare | Ilustração Especial Rara (SAR) | bg-danger |
| Art Rare | Ilustração Rara (AR) | bg-warning text-dark |
| Hyper Rare | Hyper Rare (HR) | bg-warning text-dark |
| Shiny Rare | Shiny Rare (SR) | bg-success |
| Ultra Rare | Ultra Rare (UR) | bg-dark |
| Promo | Promo + descrição | bg-dark / bg-warning |
| Full Art | Full Art | bg-dark |
| Common | Common + descrição | bg-success / bg-secondary |

**Exemplos corretos:**
- ✅ "Ilustração Especial Rara (SAR)"
- ✅ "Ilustração Rara (AR)"
- ✅ "Hyper Rare (HR)"
- ✅ "Shiny Rare (SR)"
- ✅ "Ultra Rare (UR)"

**Exemplos INCORRETOS:**
- ❌ "Special Art Rare" (sem tradução)
- ❌ "Art Rare" (sem tradução)
- ❌ "Ilustração Especial Rara (SIR)" (abreviação errada)
- ❌ "Shiny Rare (S)" (abreviação incompleta)
- ❌ "Ultra Rare (GX)" (abreviação específica de tipo)

---

## Notas Importantes

1. **Consistência de Datas:** Use o formato DD/MM/YYYY
2. **Badges de Raridade:** Ajuste as cores conforme a raridade (veja tabela acima)
3. **Formato de Raridade:** SEMPRE use a padronização mista (português + abreviação inglesa)
4. **URLs das Fotos:** Sempre teste se as URLs do Cloudinary estão acessíveis
5. **Links Externos:** Verifique se todos os links estão funcionando antes de publicar
6. **Accordion:** O primeiro item do histórico deve ter `collapse show` para iniciar aberto
