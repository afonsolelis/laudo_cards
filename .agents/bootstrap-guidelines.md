# Diretrizes de Uso do Bootstrap 5

## Princípio Fundamental

**NUNCA use CSS customizado. Somente classes Bootstrap.**

## Sistema de Grid

### Container
```html
<div class="container">     <!-- Largura fixa responsiva -->
<div class="container-fluid"> <!-- 100% da largura -->
```

### Grid System
```html
<div class="row">
    <div class="col-12 col-md-6 col-lg-4">
        <!-- Conteúdo -->
    </div>
</div>
```

### Breakpoints
- `col-` : Extra small (<576px)
- `col-sm-` : Small (≥576px)
- `col-md-` : Medium (≥768px)
- `col-lg-` : Large (≥992px)
- `col-xl-` : Extra large (≥1200px)
- `col-xxl-` : Extra extra large (≥1400px)

## Componentes Principais

### Cards
```html
<div class="card">
    <div class="card-header">Título</div>
    <div class="card-body">
        <h5 class="card-title">Título do Card</h5>
        <p class="card-text">Texto</p>
    </div>
    <div class="card-footer">Rodapé</div>
</div>
```

### Badges
```html
<span class="badge bg-primary">Primário</span>
<span class="badge bg-success">Sucesso</span>
<span class="badge bg-danger">Perigo</span>
<span class="badge bg-warning text-dark">Aviso</span>
<span class="badge bg-info">Info</span>
```

### Alerts
```html
<div class="alert alert-info">
    <h6 class="alert-heading">Título</h6>
    <p>Conteúdo do alerta</p>
</div>
```

### Progress Bars
```html
<div class="progress" style="height: 30px;">
    <div class="progress-bar bg-success" role="progressbar"
         style="width: 85%;" aria-valuenow="85"
         aria-valuemin="0" aria-valuemax="100">
        85%
    </div>
</div>
```

### Accordion
```html
<div class="accordion" id="accordionExample">
    <div class="accordion-item">
        <h2 class="accordion-header">
            <button class="accordion-button" type="button"
                    data-bs-toggle="collapse" data-bs-target="#collapse1">
                Título
            </button>
        </h2>
        <div id="collapse1" class="accordion-collapse collapse show">
            <div class="accordion-body">Conteúdo</div>
        </div>
    </div>
</div>
```

## Utilities Essenciais

### Spacing (Margin e Padding)
- `m-*` : margin
- `p-*` : padding
- `mt-*`, `mb-*`, `ms-*`, `me-*` : margin top, bottom, start, end
- `pt-*`, `pb-*`, `ps-*`, `pe-*` : padding top, bottom, start, end
- Tamanhos: 0, 1, 2, 3, 4, 5 (0rem, 0.25rem, 0.5rem, 1rem, 1.5rem, 3rem)

### Cores
**Background:**
- `bg-primary`, `bg-secondary`, `bg-success`, `bg-danger`, `bg-warning`, `bg-info`, `bg-light`, `bg-dark`, `bg-white`

**Text:**
- `text-primary`, `text-secondary`, `text-success`, `text-danger`, `text-warning`, `text-info`, `text-light`, `text-dark`, `text-white`, `text-muted`

### Texto
- `text-center`, `text-start`, `text-end`
- `fw-bold`, `fw-normal`, `fw-light`
- `fs-1` até `fs-6` (tamanhos de fonte)
- `lead` (parágrafo destacado)
- `display-1` até `display-6` (headings grandes)

### Bordas
- `border`, `border-top`, `border-bottom`, `border-start`, `border-end`
- `border-primary`, `border-success`, `border-danger`, etc.
- `rounded`, `rounded-circle`, `rounded-pill`

### Sombras
- `shadow-sm` : sombra pequena
- `shadow` : sombra média
- `shadow-lg` : sombra grande

### Display
- `d-none`, `d-block`, `d-inline`, `d-flex`
- Responsivo: `d-none d-md-block` (esconde em mobile, mostra em md+)

### Flexbox
- `d-flex`
- `justify-content-start`, `justify-content-center`, `justify-content-end`, `justify-content-between`
- `align-items-start`, `align-items-center`, `align-items-end`

## Botões

```html
<button class="btn btn-primary">Primário</button>
<button class="btn btn-success">Sucesso</button>
<button class="btn btn-danger">Perigo</button>

<!-- Tamanhos -->
<button class="btn btn-primary btn-sm">Pequeno</button>
<button class="btn btn-primary">Normal</button>
<button class="btn btn-primary btn-lg">Grande</button>

<!-- Largura total -->
<button class="btn btn-primary w-100">Largura Total</button>
```

## Navbar

```html
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container">
        <a class="navbar-brand" href="#">Logo</a>
        <button class="navbar-toggler" type="button"
                data-bs-toggle="collapse" data-bs-target="#navbarNav">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ms-auto">
                <li class="nav-item">
                    <a class="nav-link active" href="#">Home</a>
                </li>
            </ul>
        </div>
    </div>
</nav>
```

## Cores para Tipos Pokémon

Sugestões de cores Bootstrap para tipos:
- **Fogo**: `bg-danger` ou `bg-warning`
- **Água**: `bg-info` ou `bg-primary`
- **Planta**: `bg-success`
- **Elétrico**: `bg-warning text-dark`
- **Psíquico**: `bg-primary`
- **Normal**: `bg-secondary`
- **Lutador**: `bg-secondary`

## Lista de Grupos

```html
<ul class="list-group">
    <li class="list-group-item">Item 1</li>
    <li class="list-group-item">Item 2</li>
    <li class="list-group-item active">Item Ativo</li>
</ul>

<ul class="list-group list-group-flush">
    <!-- Sem bordas nas laterais -->
</ul>
```

## Regras de Ouro

1. ✅ Use sempre classes Bootstrap nativas
2. ✅ Combine classes para obter o efeito desejado
3. ✅ Use o sistema de grid responsivo
4. ✅ Aproveite as utility classes
5. ❌ NUNCA crie CSS customizado
6. ❌ NUNCA use style inline (exceto para progress width)
