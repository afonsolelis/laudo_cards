# Skill: Perícia Template

## 📋 Descrição

Skill que automatiza a criação de páginas de perícia de cartas Pokémon TCG graduadas, usando o template padronizado do projeto.

## 🎯 Como Usar

Esta skill é **invocada automaticamente** pelo Claude quando você:

- Pedir para criar uma nova perícia
- Solicitar adicionar uma nova carta ao portfólio
- Mencionar "criar laudo de carta"
- Dizer "nova perícia para [nome da carta]"

### Exemplos de Comandos

```
"Criar perícia para o Charizard ex"
"Adicionar nova carta ao portfólio - Pikachu VMAX"
"Quero criar um laudo para o Mewtwo GX"
"Nova perícia para Ancient Mew"
```

## 📁 Estrutura da Skill

```
pericia-template/
├── SKILL.md          # Instruções principais da skill
├── reference.md      # Referência completa de variáveis (TEMPLATE_GUIDE.md)
├── examples.md       # Exemplos de uso
└── README.md         # Este arquivo
```

## 🔧 O Que a Skill Faz

1. **Coleta informações** através de perguntas interativas
2. **Lê o template** em `template_pericia.html`
3. **Substitui variáveis** pelos dados coletados
4. **Calcula cores** dos badges automaticamente
5. **Gera conteúdo dinâmico** (histórico, observações)
6. **Salva o arquivo** em `pages/[nome-carta].html`
7. **Valida** o resultado final

## 📊 Dados Coletados

### Informações Básicas
- Nome, número, coleção, ano, raridade
- Tipo, idioma, fabricante, ilustrador
- URLs das fotos (frente e verso)

### Informações de Graduação
- Graduadora (Manafix ou GBA)
- Certificado e nota final
- Notas detalhadas (Centering, Corners, Edges, Surface)
- Ranking/População

### Conteúdo Dinâmico
- Observações técnicas detalhadas
- Histórico de proveniência
- Informações sobre o artista
- Links de referência

## 🎨 Recursos Automáticos

### Cores de Badge
A skill calcula automaticamente as cores baseado nas notas:
- **9.5-10:** Verde (bg-success)
- **8-9:** Amarelo (bg-warning)
- **<8:** Cinza (bg-secondary)

### Nome do Arquivo
Converte automaticamente para kebab-case:
- "Pikachu ex" → `pikachu-ex.html`
- "Mew Ancestral" → `mew-anciao.html`

### IDs Únicos
Gera IDs únicos para os itens do accordion do histórico.

## 🔍 Validação

Antes de salvar, a skill verifica:
- ✅ Todas as variáveis foram substituídas
- ✅ URLs estão corretas
- ✅ Cores dos badges correspondem às notas
- ✅ Estrutura HTML está válida
- ✅ IDs do accordion são únicos

## 📚 Referência Completa

Para ver todas as variáveis disponíveis e exemplos detalhados, consulte:
- [reference.md](reference.md) - Guia completo de variáveis
- [examples.md](examples.md) - Exemplos de uso

## 🚀 Próximos Passos Após Criar

1. ✅ Página criada em `pages/[nome].html`
2. 📝 Adicionar link na `index.html`
3. 🌐 Testar no navegador
4. 🔗 Verificar todos os links externos
5. 📱 Testar responsividade mobile

## 💡 Dicas

- **Dados completos:** Quanto mais informações você fornecer, menos perguntas serão feitas
- **Copy/paste:** Você pode colar todos os dados de uma vez
- **Estrutura flexível:** A skill se adapta a diferentes graduadoras e formatos
- **Consistência:** Mantém o padrão das páginas existentes

## 🐛 Troubleshooting

Se a skill não for ativada automaticamente:
1. Use palavras-chave claras ("criar perícia", "nova carta")
2. Mencione o nome da carta
3. Verifique se está no diretório correto do projeto

## 📖 Exemplos Rápidos

### Exemplo 1: Mínimo
```
Usuário: "Criar perícia para Mewtwo ex"
Skill: [Faz perguntas para coletar informações]
```

### Exemplo 2: Completo
```
Usuário: "Criar perícia para Charizard ex, GBA nota 9, certificado P123456..."
Skill: [Usa dados fornecidos e pergunta apenas o que falta]
```

### Exemplo 3: Customizado
```
Usuário: "Nova perícia para Ancient Mew, usar estrutura estilo Mew Ancião"
Skill: [Aplica o padrão solicitado]
```

---

**Versão:** 1.0
**Última atualização:** 25/12/2025
**Autor:** Afonso Lelis
