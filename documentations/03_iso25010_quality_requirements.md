# Requisitos de Qualidade (ISO/IEC 25010) e SWEBOK 4.0

Como guardião da engenharia de qualidade (@po e @qa), a arquitetura não-funcional do sistema foi fundamentada nos 8 eixos do modelo de qualidade de software ISO/IEC 25010.

## 1. Adequação Funcional (Functional Suitability)
A capacidade do software de fornecer funções que atendam às necessidades declaradas e implícitas.
- **RNF-01.1 (Completude):** O sistema deve abranger 100% dos dados essenciais contidos em slabs físicos das maiores empresas de graduação do mundo (PSA, BGS, CGC), suportando campos de *Subgrades*.
- **RNF-01.2 (Correção Funcional):** A lógica de validação de formulários não deve permitir a inserção de *Subgrades* maiores que 10.0 ou negativos, nem notas finais fora do escopo validado.

## 2. Eficiência de Desempenho (Performance Efficiency)
A performance sob condições determinadas de recursos.
- **RNF-02.1 (Comportamento de Tempo):** O tempo de carregamento da galeria pública não deve exceder 2 segundos em conexões 4G padrão.
- **RNF-02.2 (Utilização de Recursos):** O upload de imagens deve obrigatoriamente fazer *offload* (delegação) para uma CDN especializada (Cloudinary) a fim de poupar I/O, armazenamento em disco local e gargalos de rede do servidor principal no Railway.

## 3. Compatibilidade (Compatibility)
O grau com que o software pode compartilhar informações ou realizar suas funções num mesmo ambiente (interoperabilidade/coexistência).
- **RNF-03.1 (Interoperabilidade):** A API do projeto (`FastAPI`) deve respeitar princípios RESTful (HTTP GET/POST) e formatar o contrato em rotas que possam ser consumidas tanto pelas templates Jinja2 (SSR) quanto via JSON puro se houver necessidade de aplicativo mobile no futuro.

## 4. Usabilidade (Usability)
A facilidade de compreensão, aprendizado e uso.
- **RNF-04.1 (Estética e Minimalismo):** O sistema deve aplicar Design Tokens Dark Mode Premium e *Glassmorphism* para destacar de forma luxuosa as cartas, focando a atenção na arte e nota técnica.
- **RNF-04.2 (Operabilidade):** A navegação entre o Admin Dashboard e a página da Carta deve acontecer no máximo com 2 cliques, mantendo o padrão UX de "lista" -> "detalhe".

## 5. Confiabilidade (Reliability)
A capacidade de manter um nível especificado de desempenho por um período de tempo.
- **RNF-05.1 (Maturidade e Tolerância a Falhas):** O servidor web backend deve processar a recuperação de falhas via Uvicorn workers e o container Docker (`Nixpacks` no Railway) deve se autorrecuperar (Restart Policy) se a aplicação "craschar".
- **RNF-05.2 (Disponibilidade):** O banco de dados (MongoDB) deve estar hospedado em rede gerida para garantir uptime de 99.9%.

## 6. Segurança (Security)
Proteção de dados e informações contra pessoas ou sistemas não autorizados.
- **RNF-06.1 (Confidencialidade e Integridade):** Somente o administrador autenticado via sessão criptografada tem permissão para inserir, editar ou apagar registros. O acesso externo ao painel é negado (`HTTP 401 Unauthorized`).
- **RNF-06.2 (Criptografia):** Senhas do administrador nunca podem ser salvas em texto puro (plain-text). Apenas *hashes* matematicamente unidirecionais usando a biblioteca `bcrypt` são armazenados no banco de dados.

## 7. Manutenibilidade (Maintainability)
Eficácia com que modificações e correções podem ser feitas pelo time de engenharia.
- **RNF-07.1 (Modularidade):** O backend deve estar isolado da apresentação visual (Padrão MVC-like), dividindo responsabilidades entre `main.py` (Rotas), `models.py` (Modelagem), `database.py` (Persistência) e `storage.py` (Mídia).
- **RNF-07.2 (Testabilidade):** A aplicação deve suportar uma suíte de testes de integração via `pytest` validando respostas HTTP das rotas principais antes de qualquer deploy em produção.

## 8. Portabilidade (Portability)
Capacidade do software ser transferido de um ambiente para outro.
- **RNF-08.1 (Adaptabilidade de Nuvem):** O sistema deve ser independente de nuvem proprietária (*Cloud Agnostic Architecture*), não usando serviços atrelados permanentemente a um fornecedor (AWS/GCP lock-in), podendo rodar no Railway, Heroku ou num servidor VPS próprio contanto que tenham as variáveis de ambiente setadas em um `.env`.
- **RNF-08.2 (Facilidade de Instalação):** A declaração de pacotes via `requirements.txt` assegura compatibilidade com os buildpacks padrão Python.
