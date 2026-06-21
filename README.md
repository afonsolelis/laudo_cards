# Laudo Cards 🎴

Um portfólio digital seguro e premium para colecionadores de Cartas Pokémon TCG Graduadas. Esta plataforma permite que colecionadores exibam seu acervo de *slabs* com o máximo de clareza, documentação rigorosa de condição (subgrades) e links de referência de mercado.

## 🌟 Destaques e Features

- **Catálogo Premium:** Interface *Dark Mode Premium* com tipografia elegante e *Glassmorphism* para dar o maior destaque visual à arte e às notas técnicas das cartas.
- **Micro-interações e HUD de Colecionador:** Animações fluidas em 3D no hover e barras de progresso modernas detalhando a graduação (Centering, Corners, Edges, Surface).
- **Hospedagem de Imagens na Nuvem:** Integração nativa com Cloudinary, aliviando o servidor e acelerando a entrega via CDN global.
- **Painel Administrativo Seguro:** CRUD completo (Create, Read, Update, Delete) acessível somente após autenticação via cookies baseados em sessões criptografadas (Bcrypt).
- **Busca, Filtros e Ordenação no Client-Side:** Pesquisa ultra-rápida, filtragem por empresa certificadora e ordenação por nota máxima e mínima sem a necessidade de reloading da página.
- **Preparado para Escalar (QA Validado):** Arquitetura Server-Side Rendered (Jinja2) combinada com um backend extremamente rápido e assíncrono (FastAPI) em banco NoSQL (MongoDB), acompanhado de script de teste de carga assíncrono hiper veloz.

## 🛠️ Stack Tecnológico

A plataforma foi construída com tecnologias modernas de alto desempenho:

**Backend:**
- **[FastAPI](https://fastapi.tiangolo.com/):** Framework web assíncrono hiper veloz para Python.
- **[Motor](https://motor.readthedocs.io/):** Driver assíncrono oficial para MongoDB.
- **[Jinja2](https://jinja.palletsprojects.com/):** Engine de templates segura e extensível para renderização SSR.
- **[Bcrypt](https://pypi.org/project/bcrypt/):** Algoritmo de hash de senhas confiável.
- **[Cloudinary](https://cloudinary.com/):** SDK oficial para upload assíncrono direto do servidor.

**Frontend:**
- **HTML5 & CSS3 Vanilla:** Focado em *Design Tokens*, varíaveis HSL e animações CSS (`@keyframes`, `transition`).
- **Bootstrap 5.3:** Para sistema de grid responsivo, modais de imagem ampliada e estrutura base de componentes.
- **Tipografia do Google Fonts:** Combinação harmônica das fontes `Outfit` (Headings e Números) e `Inter` (Parágrafos).

**Infraestrutura & DevOps:**
- **[Railway](https://railway.app/):** Plataforma PaaS de nuvem para deploy sem fricção.
- **[Nixpacks](https://nixpacks.com/):** Build engine open-source usada pelo Railway para compilar a aplicação sem a necessidade de escrever `Dockerfiles` pesados manualmente.
- **[GitHub Actions](https://github.com/features/actions):** CI/CD pipeline (*Quality Gate*) rodando validações rigorosas (Pytest, Black, Flake8, Isort e Bandit).

## 🚀 Como Executar Localmente

### Pré-requisitos
- Python 3.10+
- MongoDB instalado ou cluster remoto do MongoDB Atlas.
- Conta gratuita no Cloudinary (com as credenciais de API prontas).

### 1. Clonar o repositório
```bash
git clone https://github.com/afonsolelis/laudo_cards.git
cd laudo_cards
```

### 2. Configurar o Ambiente Virtual
```bash
python -m venv venv

# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 3. Instalar Dependências
Instale os pacotes diretamente do `requirements.txt` da pasta backend (ou raiz):
```bash
pip install -r backend/requirements.txt
```

### 4. Variáveis de Ambiente (.env)
Crie um arquivo `.env` na raiz do projeto contendo as seguintes credenciais obrigatórica:
```env
# Banco de Dados
MONGO_URL=mongodb+srv://<usuario>:<senha>@cluster0.exemplo.mongodb.net/?retryWrites=true&w=majority
MONGO_DB=laudo_cards

# Credenciais do Administrador Padrão
ADMIN_USERNAME=admin
ADMIN_PASSWORD_HASH=$2b$12$exemploHashGeradoAqui...  # Hash Bcrypt da sua senha
SECRET_KEY=uma_chave_aleatoria_longa_e_segura

# Cloudinary
CLOUDINARY_CLOUD_NAME=seu_nome_de_nuvem
CLOUDINARY_API_KEY=sua_api_key
CLOUDINARY_API_SECRET=seu_api_secret
```
*Obs: Você pode usar `import bcrypt; print(bcrypt.hashpw(b"suasenha", bcrypt.gensalt()).decode('utf-8'))` em um console Python para gerar um hash Bcrypt válido.*

### 5. Iniciar o Servidor de Desenvolvimento
Rode o servidor web Uvicorn:
```bash
cd backend
uvicorn main:app --reload
```

Acesse no navegador:
- Galeria Pública: `http://localhost:8000`
- Painel Administrativo: `http://localhost:8000/login`

## 📁 Estrutura de Diretórios e Código

O código-fonte principal concentra-se dentro da pasta `/backend/`. A separação lógica é intencionalmente MVC-like:

```text
laudo_cards/
├── backend/
│   ├── main.py            # Inicialização do FastAPI e Rotas HTTP
│   ├── database.py        # Configuração assíncrona do MongoDB
│   ├── models.py          # Tipagens Pydantic e Validações
│   ├── storage.py         # Lógica de interface e upload com Cloudinary
│   ├── pdf_generator.py   # Motor gerador de PDFs (ReportLab)
│   ├── requirements.txt   # Dependências do pacote pip
│   ├── static/            # CSS, Favicon, JS customizados
│   └── templates/         # Arquivos HTML Jinja2 (Views)
├── documentations/        # UML e Requisitos de Qualidade (ISO 25010)
├── .github/               # Workflows de CI/CD (Actions) e Agentes
└── requirements.txt       # Arquivo "proxy" para Nixpacks / Railway
```

## 📜 Licença
Este projeto é provido "as-is", criado inicialmente como uma coleção pessoal particular. Dependências open source estão sujeitas às suas próprias licenças.

---
Desenvolvido e padronizado sob rigorosos eixos de qualidade de software.
