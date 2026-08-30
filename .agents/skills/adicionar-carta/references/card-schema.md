# Schema de cadastro de carta

Este guia espelha `backend/models.py` e os valores oferecidos por
`backend/templates/admin.html`. Se houver divergência, o código atual é a fonte
de verdade e esta referência deve ser atualizada no mesmo trabalho.

## Payload

Campos obrigatórios no nível superior:

| Campo | Tipo | Regra |
|---|---|---|
| `name` | string | Nome curto exibido na galeria |
| `number` | string | Número impresso, preservando formato |
| `full_name` | string | Título completo da carta |
| `set_name` | string | Coleção/set |
| `year` | inteiro | Ano de lançamento |
| `rarity` | string | Valor canônico da lista abaixo |
| `pokemon_type` | string | Valor canônico da lista abaixo |
| `language` | string | Valor canônico da lista abaixo |
| `illustrator_name` | string | Artista/ilustrador impresso |
| `grading_company` | string | Nome exato existente em `graders` |
| `certificate_number` | string | Certificado como texto |
| `grading_year` | inteiro | Ano da certificação |
| `grade` | objeto | Exige `final` e `description` |
| `links` | objeto | Pode ser `{}` |

Campos opcionais:

| Campo | Tipo | Observação |
|---|---|---|
| `acquisition_price` | número ou null | Valor pago, nunca estimativa de mercado |
| `added_date` | `YYYY-MM-DD` ou null | O utilitário preenche a data atual se ausente |
| `available_for_trade` | boolean | Padrão `false` |
| `cert_link` | URL ou null | Consulta pública oficial |
| `image_front_url` | URL ou null | Obrigatória para inclusão normal |
| `image_back_url` | URL ou null | Obrigatória para inclusão normal |
| `grader_notes_markdown` | string ou null | Observações técnicas exibidas no laudo |
| `card_history` | string ou null | Proveniência/histórico exibido no laudo |
| `history_markdown` | string ou null | Legado; não usar em novos cadastros |

`grade`:

```json
{
  "centering": null,
  "corners": null,
  "edges": null,
  "surface": null,
  "final": 9.0,
  "description": "Mint"
}
```

As quatro subgrades são opcionais. Todos os valores presentes devem ser
numéricos entre 1 e 10 e reproduzir o rótulo da graduadora.

`links` aceita apenas:

```json
{
  "tcg_player": null,
  "price_charting": null,
  "liga_pokemon": null,
  "myp_cards": null,
  "ebay": null
}
```

## Valores canônicos do painel

### Raridade

- `Comum (●)`
- `Incomum (◆)`
- `Rara (★)`
- `Rara Dupla (★★)`
- `Rara Ultra (★★ holográfica)`
- `Ilustração Rara (Rare Illustration)`
- `Ilustração Rara Especial (Special Illustration Rare - SIR/SAR)`
- `Rara Hiper / Secreta (★★★ dourada)`
- `Rara Holofoil`
- `Rara Reversa (Reverse Holo)`
- `Ultra Rara (Estrela Branca)`
- `Secret Rare`
- `Radiant`
- `Promo (★ PROMOG / P)`
- `Cartas de Subconjunto (Subset)`
- `Ace Spec`
- `Prism Star`

### Tipo

- `Grass (Planta)`
- `Fire (Fogo)`
- `Water (Água)`
- `Lightning (Elétrico)`
- `Psychic (Psíquico)`
- `Fighting (Lutador)`
- `Darkness (Sombrio)`
- `Metal (Metálico)`
- `Fairy (Fada)`
- `Dragon (Dragão)`
- `Colorless (Incolor)`
- `Stellar (Estelar)`
- `Trainer (Treinador)`
- `Energy (Energia)`

### Idioma

- `Inglês (English)`
- `Português (Portuguese)`
- `Japonês (Japanese)`
- `Espanhol (Spanish)`
- `Francês (French)`
- `Alemão (German)`
- `Italiano (Italian)`
- `Coreano (Korean)`
- `Chinês Tradicional (Traditional Chinese)`
- `Chinês Simplificado (Simplified Chinese)`
- `Tailandês (Thai)`
- `Indonésio (Indonesian)`
- `Holandês (Dutch)`
- `Polonês (Polish)`
- `Russo (Russian)`

Graduadoras não são hardcoded. Consulte `list-graders` e preserve exatamente o
valor armazenado na collection `graders`.

## Exemplo estrutural

```json
{
  "name": "Nome da carta",
  "number": "000/000",
  "full_name": "Nome da carta - Nome da coleção",
  "set_name": "Nome da coleção",
  "year": 2026,
  "rarity": "Rara (★)",
  "pokemon_type": "Colorless (Incolor)",
  "language": "Português (Portuguese)",
  "illustrator_name": "Nome do artista",
  "acquisition_price": null,
  "available_for_trade": false,
  "grading_company": "Graduadora existente",
  "certificate_number": "CERTIFICADO",
  "grading_year": 2026,
  "cert_link": null,
  "image_front_url": "https://exemplo.invalid/frente.jpg",
  "image_back_url": "https://exemplo.invalid/verso.jpg",
  "grade": {
    "centering": null,
    "corners": null,
    "edges": null,
    "surface": null,
    "final": 9.0,
    "description": "Mint"
  },
  "links": {},
  "grader_notes_markdown": null,
  "card_history": null
}
```

Remova URLs de exemplo e substitua todos os placeholders antes do preflight.
