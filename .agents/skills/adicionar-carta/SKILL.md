---
name: adicionar-carta
description: Cadastrar novas cartas graduadas no acervo do Laudo Cards, preparando e validando os dados, enviando imagens quando necessário e inserindo o documento com segurança no MongoDB. Use quando o usuário pedir para adicionar, cadastrar ou incluir uma carta; não use para simples mudanças de layout.
---

# Adicionar carta ao Laudo Cards

Cadastre a carta como um documento MongoDB compatível com `backend/models.py`. A
aplicação é FastAPI com templates Jinja2 dinâmicos: nunca crie uma página HTML
individual em `pages/` nem restaure o gerador estático antigo.

## Antes de começar

Leia [references/card-schema.md](references/card-schema.md) antes de preparar o
payload. Confirme também o modelo vigente em `backend/models.py` se ele tiver
mudado depois desta skill.

Use como evidência, nesta ordem:

1. dados e imagens fornecidos pelo usuário;
2. texto legível no rótulo da graduadora e na própria carta;
3. página pública do certificado e fontes de catálogo confiáveis, quando
   necessárias.

Não invente certificado, nota, subgrades, preço de aquisição, proveniência ou
URLs. Pesquise metadados públicos somente quando faltarem e deixe claro o que
foi inferido. Faça perguntas apenas sobre campos obrigatórios que não possam ser
obtidos com segurança das evidências disponíveis.

## Autorização

Um pedido explícito para "adicionar", "cadastrar" ou "incluir" uma carta
autoriza a criação desse documento e o upload das duas imagens necessárias. Um
pedido para apenas analisar, pesquisar, revisar ou preparar os dados autoriza
somente validação e preflight; não grave no banco.

Esta skill não autoriza editar ou excluir cartas existentes. Se o preflight
encontrar uma carta com a mesma graduadora e o mesmo certificado, pare e informe
o `_id` existente. Só faça uma atualização após um pedido explícito do usuário.

## Fluxo

1. Reúna os campos obrigatórios do schema. Preserve exatamente números de carta
   e certificado, inclusive zeros, barras, hífens e letras.
2. Inspecione as fotos quando elas forem fornecidas. Frente e verso são
   obrigatórios para uma inclusão normal; aceite ausência somente se o usuário
   pedir explicitamente para cadastrar incompleto.
3. Use os valores canônicos do painel administrativo para raridade, tipo e
   idioma. O nome da graduadora deve corresponder exatamente a um registro da
   collection `graders`.
4. Crie um JSON temporário fora do repositório, sem `_id`, seguindo
   `references/card-schema.md`. Use `links: {}` quando não houver links.
5. Execute o preflight read-only:

   ```bash
   uv run --with-requirements backend/requirements.txt \
     python .agents/skills/adicionar-carta/scripts/card_admin.py \
     preflight --input /tmp/carta.json
   ```

   O preflight valida o `CardModel`, consulta a graduadora e procura duplicata
   por `grading_company + certificate_number`.
6. Mostre ao usuário um resumo conciso antes da gravação somente quando houver
   alguma escolha ou inferência material pendente. Se o pedido já contiver dados
   inequívocos e autorização para incluir, prossiga.
7. Cadastre usando URLs de imagem já existentes no payload ou arquivos locais:

   ```bash
   uv run --with-requirements backend/requirements.txt \
     python .agents/skills/adicionar-carta/scripts/card_admin.py \
     create --input /tmp/carta.json \
     --front-image /caminho/frente.jpg \
     --back-image /caminho/verso.jpg
   ```

   Omita `--front-image` ou `--back-image` quando o respectivo URL já estiver no
   JSON. O utilitário envia arquivos locais ao Cloudinary antes da inserção.
   Use `--allow-missing-images` somente quando o usuário tiver pedido
   explicitamente um cadastro incompleto.
8. Verifique o resultado retornado pelo utilitário. Informe o ObjectId, o nome
   da carta e a rota `/laudo/{id}`. Não exponha o `MONGO_URL`, credenciais do
   Cloudinary ou outros segredos.

## Regras de integridade

- Considere `grading_company + certificate_number` a chave natural de uma
  carta graduada.
- `added_date` deve ser a data de inclusão real em `YYYY-MM-DD`; quando omitida,
  o utilitário usa a data atual.
- Notas devem refletir o rótulo. Não calcule subgrades ausentes nem force a nota
  final a ser média dos componentes.
- Use `card_history` para proveniência/histórico exibido no laudo e
  `grader_notes_markdown` para observações técnicas. `history_markdown` é legado
  e não é renderizado pelo template atual.
- Não marque `available_for_trade` como verdadeiro sem instrução explícita.
- Não salve arquivos temporários, imagens fornecidas ou payloads com dados de
  aquisição no Git.
- Se upload ou inserção falhar, não anuncie sucesso. O utilitário tenta remover
  uploads feitos durante a operação quando o banco não é gravado.

## Diagnóstico

Para listar as graduadoras aceitas sem alterar dados:

```bash
uv run --with-requirements backend/requirements.txt \
  python .agents/skills/adicionar-carta/scripts/card_admin.py list-graders
```

Se a rede do ambiente estiver bloqueada, solicite autorização para executar o
mesmo comando com acesso de rede. Não contorne a restrição nem copie a URI para
a linha de comando.
