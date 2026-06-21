# Diagramas UML de Modelagem (Mermaid)

Este documento centraliza a arquitetura visual do Laudo Cards para facilitar o entendimento técnico e onboarding de novos engenheiros.

## 1. UML de Classes (Domínio de Dados)

O banco de dados é um MongoDB NoSQL, mas conceitualmente modelamos as entidades da seguinte forma:

```mermaid
classDiagram
    class User {
        +ObjectId _id
        +String username
        +String password_hash
        +login(username, password) bool
    }

    class Card {
        +ObjectId _id
        +String name
        +String full_name
        +String set_name
        +String number
        +String year
        +String rarity
        +String pokemon_type
        +String language
        +String illustrator_name
        +String certificate_number
        +String grading_company
        +String grading_year
        +String cert_link
        +String image_front_url
        +String image_back_url
        +String grader_notes_markdown
        +String card_history
        +save() ObjectId
        +update(data) bool
        +delete() bool
    }

    class Grade {
        +Float final
        +Float centering
        +Float corners
        +Float edges
        +Float surface
        +String description
    }

    class Links {
        +String tcg_player
        +String price_charting
        +String liga_pokemon
        +String myp_cards
    }

    Card "1" *-- "1" Grade : contains
    Card "1" *-- "1" Links : contains
```

## 2. UML de Sequência: Autenticação Administrativa

Fluxo demonstrando como a persistência de sessão foi implementada com Cookies criptografados (FastAPI e bcrypt).

```mermaid
sequenceDiagram
    actor Admin
    participant Frontend as laudo.html / admin.html
    participant Backend as FastAPI App
    participant DB as MongoDB (users)
    
    Admin->>Frontend: Acessa /login
    Admin->>Frontend: Preenche Credenciais (POST /login)
    Frontend->>Backend: Envia Form (username, password)
    Backend->>DB: find_one(username)
    DB-->>Backend: Retorna User Doc (password_hash)
    Backend->>Backend: bcrypt.checkpw(password, hash)
    alt Senha Válida
        Backend->>Backend: Cria JWT ou Session Token
        Backend-->>Frontend: Redireciona /admin + Set-Cookie "session"
        Frontend-->>Admin: Exibe Painel de Administração
    else Senha Inválida
        Backend-->>Frontend: Redireciona /login?error=1
        Frontend-->>Admin: Exibe "Usuário ou senha inválidos"
    end
```

## 3. UML de Sequência: Upload de Mídia (Cloudinary)

Fluxo demonstrando o armazenamento na nuvem e a inserção no banco de dados.

```mermaid
sequenceDiagram
    actor Admin
    participant AdminUI as Painel Admin (Form)
    participant FastAPI as Backend (storage.py)
    participant Cloudinary as Cloudinary API
    participant MongoDB as Banco de Dados
    
    Admin->>AdminUI: Anexa Fotos (Frente e Verso) + Dados
    AdminUI->>FastAPI: POST /api/cards (Multipart Form)
    FastAPI->>Cloudinary: upload(file_front)
    Cloudinary-->>FastAPI: Retorna image_front_url
    FastAPI->>Cloudinary: upload(file_back)
    Cloudinary-->>FastAPI: Retorna image_back_url
    FastAPI->>FastAPI: Valida e compila Objeto Card
    FastAPI->>MongoDB: insert_one(Card)
    MongoDB-->>FastAPI: Retorna _id
    FastAPI-->>AdminUI: 303 Redirect para /admin
    AdminUI-->>Admin: Toast "Carta Adicionada com Sucesso"
```
