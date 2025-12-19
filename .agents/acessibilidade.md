# Práticas de Acessibilidade

## Princípios WCAG 2.1

Este projeto segue as diretrizes WCAG 2.1 nível AA.

## 1. Estrutura Semântica

### Hierarquia de Headings
```html
<!-- Correto -->
<h1>Título Principal</h1>
  <h2>Seção</h2>
    <h3>Subseção</h3>
  <h2>Outra Seção</h2>

<!-- Incorreto - não pule níveis -->
<h1>Título</h1>
  <h3>Subseção</h3> ❌
```

### Tags Semânticas
Use as tags corretas:
- `<nav>` para navegação
- `<main>` para conteúdo principal (se aplicável)
- `<section>` para seções de conteúdo
- `<article>` para conteúdo independente
- `<footer>` para rodapé

## 2. ARIA (Accessible Rich Internet Applications)

### Roles
```html
<div role="progressbar" aria-valuenow="85" aria-valuemin="0" aria-valuemax="100">
```

### Labels
```html
<button aria-label="Fechar menu">✕</button>
```

### Live Regions (se necessário)
```html
<div aria-live="polite">Conteúdo que muda dinamicamente</div>
```

## 3. Navegação por Teclado

### Ordem de Tab
- Garanta que a ordem de tab seja lógica
- Elementos focáveis: links, botões, inputs
- Não use `tabindex` positivo

### Indicadores de Foco
Bootstrap já fornece estilos de foco, mas verifique que estejam visíveis.

## 4. Contraste de Cores

### Requisitos WCAG AA
- Texto normal: mínimo 4.5:1
- Texto grande (≥18pt ou ≥14pt bold): mínimo 3:1

### Combinações Bootstrap Seguras
✅ `bg-dark` + `text-white`
✅ `bg-primary` + `text-white`
✅ `bg-light` + `text-dark`
✅ `bg-warning` + `text-dark`

⚠️ Evite:
❌ `bg-warning` + texto padrão (use `text-dark`)
❌ Cores claras em fundos claros

## 5. Imagens e Conteúdo Visual

### Atributo Alt
```html
<!-- Imagem informativa -->
<img src="pikachu.png" alt="Carta Pikachu Base Set">

<!-- Imagem decorativa (emojis neste projeto) -->
<div aria-hidden="true">🔥</div>
```

### Emojis
Como usamos emojis decorativos:
```html
<div class="display-1" aria-hidden="true">🔥</div>
<h2>Charizard</h2>
```

## 6. Formulários (se aplicável no futuro)

### Labels
```html
<label for="nome">Nome:</label>
<input type="text" id="nome" name="nome">
```

### Mensagens de Erro
```html
<input aria-invalid="true" aria-describedby="error-nome">
<div id="error-nome">O nome é obrigatório</div>
```

## 7. Links e Botões

### Texto Descritivo
```html
<!-- Bom -->
<a href="charizard.html">Ver detalhes do Charizard</a>

<!-- Ruim -->
<a href="charizard.html">Clique aqui</a> ❌
```

### Área de Clique
- Botões e links devem ter área mínima de 44x44px
- Bootstrap já garante isso com `.btn`

## 8. Componentes Interativos

### Accordion
Bootstrap já inclui ARIA correto:
```html
<button class="accordion-button"
        aria-expanded="true"
        aria-controls="collapse1">
```

### Navbar Toggle
```html
<button class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Alternar navegação">
    <span class="navbar-toggler-icon"></span>
</button>
```

## 9. Responsividade e Zoom

### Viewport
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

### Zoom
- Conteúdo deve ser legível até 200% de zoom
- Não use `maximum-scale=1.0` (bloqueia zoom)

## 10. Idioma

### Tag HTML
```html
<html lang="pt-BR">
```

### Mudanças de Idioma
```html
<span lang="en">Base Set</span>
```

## 11. Checklist de Acessibilidade

Para cada página, verifique:

✅ Lang definido no HTML
✅ Hierarquia de headings correta
✅ Alt text em imagens (ou aria-hidden para decorativas)
✅ Contraste de cores adequado
✅ Links com texto descritivo
✅ Navegação por teclado funcional
✅ ARIA labels onde necessário
✅ Navbar com aria correto
✅ Progress bars com role e aria-value
✅ Accordion com aria-expanded e aria-controls

## 12. Testes de Acessibilidade

### Testes Manuais
1. Navegue apenas com teclado (Tab, Enter, Espaço)
2. Use leitor de tela (NVDA, JAWS, VoiceOver)
3. Teste com 200% de zoom
4. Desative CSS e veja se conteúdo faz sentido

### Ferramentas Automatizadas
- axe DevTools
- WAVE
- Lighthouse (Chrome DevTools)

## 13. Boas Práticas Específicas do Projeto

### Progress Bars
```html
<div class="progress" style="height: 30px;">
    <div class="progress-bar bg-success"
         role="progressbar"
         style="width: 85%;"
         aria-valuenow="85"
         aria-valuemin="0"
         aria-valuemax="100">
        <span class="fw-bold">Near Mint (85%)</span>
    </div>
</div>
```

### Badges
Não precisam de ARIA especial, são puramente visuais:
```html
<span class="badge bg-danger">Fogo</span>
```

### Cards
Use headings apropriados dentro dos cards:
```html
<div class="card">
    <div class="card-header">
        <h4>📋 Perícia Técnica</h4>
    </div>
</div>
```

## Recursos

- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [Bootstrap Accessibility](https://getbootstrap.com/docs/5.3/getting-started/accessibility/)
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
