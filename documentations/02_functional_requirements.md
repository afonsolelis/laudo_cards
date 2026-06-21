# Requisitos Funcionais (RF)

Com base nas entregas realizadas, o backlog funcional do sistema Laudo Cards está formalizado abaixo para rastreabilidade SWEBOK 4.0.

| ID | Título | Descrição | Criticidade | Status |
|---|---|---|---|---|
| **RF01** | **Catálogo Público de Cartas** | O sistema deve permitir que usuários não autenticados visualizem a lista completa de cartas graduadas em formato de grade (grid), exibindo imagens, nomes e notas finais. | Alta | Concluído |
| **RF02** | **Filtros e Ordenação de Acervo** | O sistema deve permitir a busca textual por nome de carta, filtragem dinâmica por certificadora cadastrada, e ordenação de notas (Maior para Menor e vice-versa) no lado do cliente. | Média | Concluído |
| **RF03** | **Visualização de Laudo Detalhado** | O sistema deve possuir uma página dedicada por carta (HUD de Colecionador), exibindo quebra técnica das notas (Centering, Edges, Surface, Corners) e metadados completos. | Alta | Concluído |
| **RF04** | **Autenticação Segura** | O sistema deve possuir uma área restrita (`/admin`) acessível apenas mediante login com usuário e senha armazenados com hash seguro (Bcrypt) no banco de dados, utilizando persistência de sessão via Cookies. | Alta | Concluído |
| **RF05** | **CRUD Completo de Cartas** | O administrador autenticado deve ser capaz de criar (adicionar), ler (listar), atualizar (editar) e deletar (excluir) cartas diretamente no banco de dados através de um painel de controle interativo. | Alta | Concluído |
| **RF06** | **Upload e Hospedagem de Imagens** | O sistema deve permitir o envio de imagens (Frente e Verso) nos formulários de criação e edição. O backend deve processar, comprimir e realizar upload remoto no Cloudinary, salvando apenas as URLs públicas no banco de dados. | Alta | Concluído |
| **RF07** | **Visualização Ampliada de Mídia (Modal)** | A interface pública do Laudo Detalhado deve permitir o zoom (abertura em Modal Bootstrap) das fotos frontal e traseira das cartas para averiguação de autenticidade pelos visitantes. | Média | Concluído |
| **RF08** | **Links Externos de Mercado** | O sistema deve permitir o cadastro de até 4 links de referência de mercado (TCGPlayer, Price Charting, Liga Pokémon, MYP Cards) e redirecionar os visitantes mediante clique. | Baixa | Concluído |
