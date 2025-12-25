# Skills do Projeto Cartas Graduadas

Este diretório contém skills customizadas para o Claude Code que automatizam e padronizam o desenvolvimento do projeto de Cartas Pokémon TCG Graduadas.

## 📚 Skills Disponíveis

### 1. **pericia-template**
Automatiza a criação de novas páginas de perícia de cartas graduadas.

**Quando usar:**
- "Criar perícia para [carta]"
- "Adicionar nova carta ao portfólio"
- "Fazer laudo para [carta]"

**O que faz:**
- Coleta informações da carta
- Gera HTML completo usando template
- Calcula cores automaticamente
- Valida resultado final

**Arquivos:**
- `SKILL.md` - Instruções principais
- `reference.md` - Guia completo de variáveis
- `examples.md` - Exemplos de uso
- `README.md` - Documentação

---

### 2. **acessibilidade**
Garante práticas de acessibilidade WCAG 2.1 AA em todo o código HTML.

**Quando usar:**
- Ao criar ou modificar páginas HTML
- Adicionar componentes interativos
- Mencionar "acessibilidade", "ARIA", "contraste"

**O que faz:**
- Valida estrutura semântica
- Verifica ARIA attributes
- Garante contraste de cores adequado
- Valida navegação por teclado
- Checa alt text em imagens

**Princípios:**
- Perceptível
- Operável
- Compreensível
- Robusto

---

### 3. **bootstrap-guidelines**
Garante uso correto do Bootstrap 5 sem CSS customizado.

**Quando usar:**
- Criar ou modificar HTML
- Estilizar componentes
- Ajustar layout e responsividade
- Mencionar "Bootstrap", "grid", "classes CSS"

**O que faz:**
- Aplica classes Bootstrap corretas
- Garante grid system responsivo
- Usa componentes Bootstrap nativos
- Evita CSS inline desnecessário

**Princípio fundamental:**
🚫 **ZERO CSS customizado. SOMENTE Bootstrap.**

---

### 4. **codigo-html**
Define padrões de código HTML limpo e consistente.

**Quando usar:**
- Criar novos arquivos HTML
- Modificar estrutura de páginas
- Revisar ou refatorar código

**O que faz:**
- Garante indentação consistente (4 espaços)
- Aplica estrutura semântica HTML5
- Padroniza ordem de atributos
- Valida formatação e comentários

**Padrões:**
- Semântica HTML5
- Indentação de 4 espaços
- Comentários descritivos
- Atributos ordenados

---

### 5. **estrutura-paginas**
Define estrutura padrão para páginas de cartas individuais.

**Quando usar:**
- Criar novas páginas de carta
- Revisar estrutura existente
- Mencionar "layout de perícia", "estrutura de carta"

**O que faz:**
- Define seções obrigatórias
- Padroniza componentes
- Garante responsividade
- Valida completude da página

**Estrutura padrão:**
1. Navbar
2. Header
3. Fotos e Identificação
4. Graduação
5. Análise de Condição
6. Histórico
7. Footer
8. Modals

---

## 🎯 Como as Skills São Ativadas

As skills são **ativadas automaticamente** pelo Claude quando você usa palavras-chave ou comandos relacionados. Você não precisa invocá-las manualmente.

### Exemplos:

```bash
# Ativa pericia-template
"Criar perícia para Charizard"
"Nova carta - Pikachu VMAX"

# Ativa acessibilidade
"Verificar acessibilidade desta página"
"Adicionar alt text nas imagens"

# Ativa bootstrap-guidelines
"Estilizar este card"
"Criar um grid responsivo"

# Ativa codigo-html
"Formatar este HTML"
"Corrigir indentação"

# Ativa estrutura-paginas
"Qual a estrutura padrão de uma página?"
"Falta alguma seção nesta página?"
```

## 🔄 Como as Skills Trabalham Juntas

As skills são complementares e frequentemente trabalham em conjunto:

```
pericia-template (coordena)
    ├── estrutura-paginas (define layout)
    ├── bootstrap-guidelines (aplica estilos)
    ├── codigo-html (garante código limpo)
    └── acessibilidade (valida acessibilidade)
```

### Exemplo de Fluxo:

1. **Usuário:** "Criar perícia para Mewtwo ex"
2. **pericia-template** é ativada e coordena:
   - Usa **estrutura-paginas** para layout
   - Aplica **bootstrap-guidelines** para estilos
   - Segue **codigo-html** para formatação
   - Valida com **acessibilidade**
3. Resultado: Página completa, bem-estruturada, estilizada e acessível

## 📋 Hierarquia de Skills

**Nível 1 - Coordenação:**
- `pericia-template` - Automatiza criação completa

**Nível 2 - Estrutura:**
- `estrutura-paginas` - Define layout
- `codigo-html` - Define código

**Nível 3 - Estilo:**
- `bootstrap-guidelines` - Define aparência

**Nível 4 - Qualidade:**
- `acessibilidade` - Valida inclusividade

## 🎨 Padrões do Projeto

### Cores Principais
- Background: `bg-light`
- Cards: `bg-white`
- Headers: `bg-dark` ou `bg-secondary`
- Bordas: `border-secondary`

### Responsividade
- Mobile first
- Breakpoints: md (768px), lg (992px)
- Grid: `col-12 col-lg-6` para 2 colunas

### Acessibilidade
- WCAG 2.1 AA
- ARIA em componentes interativos
- Alt text em imagens
- Navegação por teclado

### Código
- 4 espaços de indentação
- HTML5 semântico
- Zero CSS customizado
- Bootstrap 5.3.0

## 📁 Estrutura de Arquivos

```
.claude/skills/
├── README.md (este arquivo)
├── acessibilidade/
│   └── SKILL.md
├── bootstrap-guidelines/
│   └── SKILL.md
├── codigo-html/
│   └── SKILL.md
├── estrutura-paginas/
│   └── SKILL.md
└── pericia-template/
    ├── SKILL.md
    ├── reference.md
    ├── examples.md
    └── README.md
```

## 🚀 Início Rápido

### Criar Uma Nova Perícia

```bash
"Criar perícia para Charizard ex da coleção Obsidian Flames"
```

A skill `pericia-template` será ativada automaticamente e guiará você no processo.

### Verificar Acessibilidade

```bash
"Verificar acessibilidade da página pikachu-gold.html"
```

A skill `acessibilidade` analisará a página e sugerirá melhorias.

### Corrigir Formatação

```bash
"Formatar o código HTML desta página"
```

A skill `codigo-html` aplicará os padrões de formatação.

## 🔧 Manutenção

### Atualizar Skills

Skills são versionadas junto com o código do projeto via git. Para atualizar:

```bash
git pull
```

As skills atualizadas serão automaticamente carregadas pelo Claude.

### Criar Nova Skill

Para criar uma nova skill:

1. Crie diretório: `.claude/skills/nome-skill/`
2. Crie arquivo: `SKILL.md` com frontmatter YAML
3. Commit e push para compartilhar com equipe

### Desabilitar Skill

Para desabilitar temporariamente uma skill, renomeie o arquivo `SKILL.md` para `SKILL.md.disabled`.

## 📖 Documentação Adicional

- [Criando Skills](https://docs.anthropic.com/claude/docs/agent-skills)
- [Bootstrap 5.3](https://getbootstrap.com/docs/5.3/)
- [WCAG 2.1](https://www.w3.org/WAI/WCAG21/quickref/)
- [HTML5 Spec](https://html.spec.whatwg.org/)

## 🤝 Contribuindo

Skills são compartilhadas via git. Para contribuir:

1. Faça melhorias nas skills existentes
2. Teste suas alterações
3. Commit e push
4. Equipe receberá automaticamente as atualizações

## 📝 Changelog

**v1.0 - 25/12/2025**
- Criadas 5 skills principais
- Migrado de `.agents` para `.claude/skills`
- Documentação completa

---

**Versão:** 1.0
**Última atualização:** 25/12/2025
**Autor:** Afonso Lelis
