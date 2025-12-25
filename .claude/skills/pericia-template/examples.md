# Exemplos de Uso da Skill Perícia Template

## Exemplo 1: Carta Moderna GBA (Padrão Completo)

**Solicitação do Usuário:**
> "Criar perícia para o Armarouge Shiny da coleção Paldean Fates"

**Processo:**

### Passo 1: Coleta de Informações Básicas
```
Nome: Armarouge
Número: 115/091
Coleção: Paldean Fates (Destinos de Paldea)
Ano: 2024
Raridade: Shiny Rare (S)
Badge Raridade: bg-dark
Tipo: Pokémon - Stage 1
Idioma: English
Lançamento: Janeiro de 2024
Fabricante: The Pokémon Company International
Ilustrador: Souichirou Gunjima
Registro AAA: Sim
```

### Passo 2: Informações de Graduação
```
Graduadora: GBA
Certificado: P0000259
Nota Final: 9
Descrição: Mint
Data Label: Data da Avaliação
Data Valor: 20/10/2025

Notas Detalhadas:
- Centering: 9.5 (bg-success)
- Corners: 9.75 (bg-success)
- Edges: 10 (bg-success)
- Surface: 9.75 (bg-success)

Ranking:
- Mesma Nota: 1
- Nota Maior: 0
- Total: 1
- Label: População
```

### Passo 3: Decisões de Estrutura
```
Links: Opção A (dentro da graduação)
Campos Adicionais: Lançamento, Registro AAA
Observação sobre data: Sim
Footer: "Laudo gerado em: 19/12/2025"
```

### Passo 4: Arquivo Gerado
`pages/armarouge.html`

---

## Exemplo 2: Carta Vintage Manafix (Histórico Extenso)

**Solicitação do Usuário:**
> "Criar perícia para o Ancient Mew USA 2000"

**Processo:**

### Passo 1: Coleta de Informações Básicas
```
Nome: Mew Ancestral (IP/∞)
Número: IP/∞
Coleção: Promos
Ano: 2000
Raridade: Promocional
Badge Raridade: bg-dark
Tipo: Pokémon - Basic
Idioma: English
Edição: Miscellaneous Promotional Card
Versão: USA 2000 - Galaxy Foil
Fabricante: Wizards of the Coast
Artista: Tomoaki Imakuni (Imakuni?)
```

### Passo 2: Informações de Graduação
```
Graduadora: Manafix
Certificado: P00003813
Nota Final: 3 HP
Descrição: Heavy Played
Data Label: Data da Certificação
Data Valor: 10/04/2025

Notas Detalhadas:
- Centering: 9.5 (bg-dark)
- Corners: 6 (bg-secondary)
- Edges: 3 (bg-secondary)
- Surface: 3 (bg-secondary)

Ranking:
- Mesma Nota: 1
- Nota Maior: 8
- Total: 9
- Label: Total
```

### Passo 3: Decisões de Estrutura
```
Links: Opção A (dentro da graduação)
Campos Adicionais: Edição, Versão
Observação sobre data: Sim
Footer: "Laudo gerado em: 19/12/2025"
Histórico: 8 itens (extenso)
```

### Passo 4: Arquivo Gerado
`pages/mew-anciao.html`

---

## Exemplo 3: Carta com Programa Especial (Pikachu Gold)

**Solicitação do Usuário:**
> "Criar perícia para o Pikachu ex Gold da promoção Halloween"

**Processo:**

### Passo 1: Coleta de Informações Básicas
```
Nome: Pikachu ex
Número: 179/131
Coleção: Prismatic Evolutions (Evoluções Prismáticas)
Ano: 2025
Raridade: Hyper Rare (Gold)
Badge Raridade: bg-warning text-dark
Tipo: Pokémon ex Básico - Elétrico
Idioma: Português
Fabricante: The Pokémon Company International
Ilustrador: aky CG Works
Registro AAA: Sim
```

### Passo 2: Informações de Graduação
```
Graduadora: GBA
Certificado: P0000254
Nota Final: 9
Descrição: Mint
Data Label: Programa
Data Valor: Halloween GBA Promo 2025

Notas Detalhadas:
- Centering: 9.25 (bg-success)
- Corners: 8.5 (bg-warning text-dark)
- Edges: 10 (bg-success)
- Surface: 10 (bg-success)

Ranking:
- Mesma Nota: 0
- Nota Maior: 0
- Total: 1
- Label: População
```

### Passo 3: Decisões de Estrutura
```
Links: Opção B (seção separada com ícones)
Campos Adicionais: Registro AAA
Observação sobre data: Não
Footer: "Laudo gerado para: P0000254"
Histórico: 2 itens (curto)
```

### Passo 4: Arquivo Gerado
`pages/pikachu-gold.html`

---

## Exemplo 4: Fluxo Interativo Completo

**Usuário:**
> "Quero adicionar uma nova carta ao portfólio - Charizard ex"

**Assistente:**
```
Vou ajudar você a criar uma nova página de perícia para o Charizard ex!
Preciso coletar algumas informações.

[Usa AskUserQuestion para coletar informações básicas]

Pergunta 1: Qual é a graduadora desta carta?
- GBA (Recomendado para cartas modernas)
- Manafix

Pergunta 2: Você tem os links de referência?
- Sim, vou fornecer
- Não, pode deixar em branco

...

[Após coletar todas as informações]

Perfeito! Agora vou criar a página de perícia.

[Lê template_pericia.html]
[Substitui todas as variáveis]
[Gera conteúdo dinâmico]
[Salva em pages/charizard-ex.html]

✓ Página criada com sucesso em pages/charizard-ex.html!

Você pode visualizá-la abrindo o arquivo no navegador.
Não se esqueça de adicionar o link na página index.html!
```

---

## Exemplo 5: Uso Rápido com Dados Fornecidos

**Usuário:**
> "Criar perícia com esses dados: [cola todos os dados]"

**Assistente:**
```
Identificado todos os dados necessários!

Vou criar a página usando:
- Nome: [detectado]
- Graduadora: [detectado]
- Nota: [detectado]
...

[Processo automático sem perguntas adicionais se todos os dados estiverem presentes]

✓ Página criada: pages/[nome].html
```

---

## Observações de Implementação

### Cores Automáticas

O assistente deve calcular automaticamente as cores dos badges baseado nas notas:

```javascript
função definirCorBadge(nota):
  se nota >= 9.5: retornar "bg-success"
  se nota >= 9.0: retornar "bg-success"
  se nota >= 8.0: retornar "bg-warning text-dark"
  se nota >= 6.0: retornar "bg-secondary"
  senão: retornar "bg-secondary"
```

### Validação de URLs

Antes de salvar, verificar se todas as URLs seguem o padrão:
- Fotos: Cloudinary (`https://res.cloudinary.com/...`)
- Links externos: HTTPS válido

### Nome do Arquivo

Converter nome da carta para kebab-case:
```
"Pikachu ex" → "pikachu-ex.html"
"Mew Ancestral (IP/∞)" → "mew-anciao.html"
"Armarouge" → "armarouge.html"
```

### Accordion IDs

Gerar IDs únicos automaticamente:
```
collapse1, collapse2, collapse3, ...
```

E garantir que apenas o item relevante inicie expandido com `collapse show`.
