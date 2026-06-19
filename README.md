# 🎴 Cartas Pokémon TCG Graduadas (Laudo Cards)

<div align="center">

![Pokémon TCG](https://img.shields.io/badge/Pokémon-TCG-ffcc00?style=for-the-badge&logo=pokemon&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)
![MinIO](https://img.shields.io/badge/MinIO-C72C48?style=for-the-badge&logo=minio&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.0-7952b3?style=for-the-badge&logo=bootstrap&logoColor=white)

**Portfólio profissional de cartas Pokémon TCG certificadas com laudos técnicos detalhados**

</div>

---

## 📋 Sobre o Projeto

Este projeto documenta uma coleção pessoal de cartas Pokémon TCG graduadas por empresas certificadoras reconhecidas (GBA, Manafix, CAPY Games, etc.). Ele possui um sistema backend em FastAPI que gerencia e serve laudos técnicos detalhados sobre as condições, o histórico e as cotações de cada carta.

### ✨ Características Principais

- 🎯 **Laudos Técnicos Profissionais** - Análise completa gerada dinamicamente
- 📊 **Sistema de Notas Detalhado** - Visualização clara com badges e barras de progresso
- 🖼️ **Armazenamento Seguro de Imagens** - Integração com MinIO via S3-compatible API
- 💾 **Persistência de Dados** - Catálogo mantido em banco MongoDB
- 📱 **Design Responsivo** - Interface web clean baseada em Bootstrap e templates Jinja2

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Função |
|------------|--------|
| **FastAPI** (Python) | Framework Backend e roteamento de páginas |
| **MongoDB** | Banco de Dados NoSQL para salvar as cartas |
| **MinIO** | Object Storage para upload e hospedagem das imagens |
| **Jinja2** | Motor de templates para renderização do HTML |
| **Bootstrap 5.3** | Framework CSS responsivo para o frontend |

---

## 📁 Estrutura do Projeto

```
laudo_cards/
│
├── backend/
│   ├── main.py               # Arquivo principal do FastAPI (Rotas)
│   ├── database.py           # Conexão com o MongoDB
│   ├── models.py             # Modelos de dados Pydantic
│   ├── storage.py            # Uploads e integração com MinIO
│   ├── requirements.txt      # Dependências Python
│   ├── static/               # Arquivos estáticos (CSS, JS, Imagens locais)
│   └── templates/            # Templates Jinja2 (HTML dinâmico)
│       ├── index.html        # Página principal do portfólio
│       └── laudo.html        # Template base do laudo da carta
│
├── README.md                 # Este arquivo
└── CLAUDE.md                 # Guia de desenvolvimento
```

---

## 🚀 Como Executar o Projeto

1. **Pré-requisitos**:
   - Python 3.9+
   - MongoDB rodando localmente ou remoto
   - Instância do MinIO configurada

2. **Configuração de Ambiente**:
   Crie um arquivo `.env` na raiz do backend com as suas credenciais (veja `.env.example`).

3. **Rodando a Aplicação**:
   ```bash
   cd backend
   pip install -r requirements.txt
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```
   Acesse no navegador: `http://localhost:8000/`

---

## 🎨 Design e Acessibilidade

O layout é gerado dinamicamente com base em variáveis no Jinja2 (`{{ card.name }}`, etc). As notas (grades) definem automaticamente as cores de badges usando um helper incluído no FastAPI:
- Gem/Mint (>= 9): Verde
- Near Mint (8 - 8.9): Amarelo
- Menos de 8: Cinza

---

## 📝 Roadmap (Em Breve)

- [ ] Painel Administrativo para cadastro manual de cartas via UI
- [ ] Integração total de rotas na API de Uploads
- [ ] Melhorias no sistema de tags e categorias
- [ ] Exportação de laudos em PDF

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
