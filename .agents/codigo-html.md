# Padrões de Código HTML

## Estrutura Básica

Toda página HTML deve seguir esta estrutura:

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>[Título da Página]</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <!-- Conteúdo -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

## Regras de Código

### 1. Indentação
- Use 4 espaços para indentação
- Mantenha consistência em todo o arquivo

### 2. Comentários HTML
- Use comentários para separar seções principais
```html
<!-- Navigation -->
<!-- Hero Section -->
<!-- Collection Section -->
<!-- Footer -->
```

### 3. Atributos
- Use aspas duplas para todos os atributos
- Ordem recomendada: class, id, data-*, title, aria-*, role

### 4. Semântica HTML5
- Use `<nav>` para navegação
- Use `<section>` para seções de conteúdo
- Use `<footer>` para rodapé
- Use `<header>` quando apropriado

### 5. Links e Navegação
- Links relativos devem usar `../` corretamente
- Botões de navegação devem ter texto descritivo

### 6. Acessibilidade
- Sempre inclua `alt` em imagens
- Use `aria-label` quando necessário
- Mantenha hierarquia de headings (h1 > h2 > h3...)

## Exemplo de Boa Prática

```html
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container">
        <a class="navbar-brand" href="../index.html">🎴 Pokémon Collection</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ms-auto">
                <li class="nav-item">
                    <a class="nav-link" href="../index.html">Voltar à Coleção</a>
                </li>
            </ul>
        </div>
    </div>
</nav>
```

## O Que Evitar

❌ CSS inline ou tags `<style>`
❌ JavaScript inline (exceto chamadas de bootstrap)
❌ Tabelas para layout
❌ Divs desnecessárias
❌ IDs duplicados
❌ Misturar português e inglês nos textos visíveis
