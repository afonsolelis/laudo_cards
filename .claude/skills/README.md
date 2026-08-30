# Skills do Projeto Cartas Graduadas

Este diretório contém skills customizadas para o Claude Code que automatizam e padronizam o desenvolvimento do projeto de Cartas Pokémon TCG Graduadas.

## 📚 Skills Disponíveis

### 1. **pericia-template**
Compatibilidade para o fluxo atual de cadastro de cartas graduadas no MongoDB.
As instruções canônicas ficam em `.agents/skills/adicionar-carta/`, para uso pelo
Codex e outros agentes compatíveis com skills de projeto.

**Quando usar:**
- "Criar perícia para [carta]"
- "Adicionar nova carta ao portfólio"
- "Fazer laudo para [carta]"

**O que faz:**
- Coleta informações da carta
- Valida os dados contra `backend/models.py`
- Confere graduadora e duplicidade de certificado
- Envia imagens ao Cloudinary quando necessário
- Insere e verifica o documento no MongoDB

**Arquivos:**
- `.claude/skills/pericia-template/SKILL.md` - Roteador de compatibilidade
- `.agents/skills/adicionar-carta/SKILL.md` - Instruções principais
- `.agents/skills/adicionar-carta/references/card-schema.md` - Schema e valores canônicos
- `.agents/skills/adicionar-carta/scripts/card_admin.py` - Preflight e cadastro seguro

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
Define a apresentação dinâmica da galeria e do laudo em templates Jinja2.

**Quando usar:**
- Alterar ou revisar `backend/templates/index.html` e `backend/templates/laudo.html`
- Mencionar "layout de laudo" ou "apresentação da carta"

**O que faz:**
- Mantém um único template para todas as cartas
- Preserva os campos condicionais do `CardModel`
- Garante responsividade e acessibilidade
- Impede a volta de páginas HTML individuais

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
    └── adicionar-carta (valida, envia imagens e persiste no MongoDB)

estrutura-paginas (somente mudanças visuais)
    ├── bootstrap-guidelines (aplica componentes)
    ├── codigo-html (garante código limpo)
    └── acessibilidade (valida acessibilidade)
```

### Exemplo de Fluxo:

1. **Usuário:** "Criar perícia para Mewtwo ex"
2. **pericia-template** é ativada e coordena:
   - Usa **adicionar-carta** para montar e validar o payload
   - Faz preflight da graduadora e do certificado
   - Envia as imagens e grava no MongoDB
3. Resultado: Carta disponível na galeria e em `/laudo/{id}` sem gerar HTML novo

## 📋 Hierarquia de Skills

**Nível 1 - Coordenação:**
- `pericia-template` - Roteia pedidos de inclusão

**Nível 2 - Persistência:**
- `adicionar-carta` - Valida e cadastra a carta no MongoDB

**Nível 3 - Estrutura visual:**
- `estrutura-paginas` - Define layout
- `codigo-html` - Define código

**Nível 4 - Estilo:**
- `bootstrap-guidelines` - Define aparência

**Nível 5 - Qualidade:**
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
    └── SKILL.md (compatibilidade)

.agents/skills/
└── adicionar-carta/
    ├── SKILL.md
    ├── references/card-schema.md
    └── scripts/card_admin.py
```

## 🚀 Início Rápido

### Criar Uma Nova Perícia

```bash
"Criar perícia para Charizard ex da coleção Obsidian Flames"
```

A skill `pericia-template` encaminhará o pedido para `adicionar-carta`, que valida
e grava a carta na aplicação dinâmica.

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
