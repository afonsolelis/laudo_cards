# 🎴 Cartas Pokémon TCG Graduadas

<div align="center">

![Pokémon TCG](https://img.shields.io/badge/Pokémon-TCG-ffcc00?style=for-the-badge&logo=pokemon&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.0-7952b3?style=for-the-badge&logo=bootstrap&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**Portfólio profissional de cartas Pokémon TCG certificadas com laudos técnicos detalhados**

[Ver Portfólio](https://afonsolelis.github.io/laudo_cards/) • [Reportar Bug](https://github.com/afonsolelis/laudo_cards/issues) • [Solicitar Feature](https://github.com/afonsolelis/laudo_cards/issues)

</div>

---

## 📋 Sobre o Projeto

Este projeto documenta uma coleção pessoal de cartas Pokémon TCG graduadas por empresas certificadoras reconhecidas (GBA, Manafix e CAPY Games). Cada carta possui uma página de laudo técnico completa com análise detalhada de condição, histórico, informações sobre ilustradores e links de referência para consulta de preços.

### ✨ Características Principais

- 🎯 **Laudos Técnicos Profissionais** - Análise completa de cada componente (Centering, Corners, Edges, Surface)
- 📊 **Sistema de Notas Detalhado** - Visualização clara das notas com barras de progresso e badges coloridos
- 🖼️ **Galeria de Imagens** - Fotos em alta qualidade da frente e verso com modal de ampliação
- 📱 **Design Responsivo** - Totalmente adaptado para desktop, tablet e mobile
- 🔍 **Links de Referência** - Integração com TCGPlayer, Price Charting, Liga Pokémon e MyP Cards
- 🎨 **Interface Moderna** - Design clean usando Bootstrap 5.3.0
- 🌐 **Múltiplas Graduadoras** - Suporte para GBA, Manafix e CAPY Games
- 📈 **Dados de População** - Informações de ranking e população de cada carta

---

## 🎴 Coleção Atual

### 📊 Estatísticas

- **Total de Cartas**: 12
- **Graduadoras**: GBA (5), Manafix (3), CAPY (4)
- **Notas**: 2x Gem Mint 10, 3x Mint 9-9.5, 2x Near Mint 8-8.5, 5x outras
- **Idiomas**: Português, Inglês, Chinês
- **Raridades**: Hyper Rare, Secret Rare, Illustration Rare, Full Art, Promo

### 🌟 Destaques da Coleção

#### Evoluções Prismáticas
- **Pikachu ex Gold** (179/131) - GBA 9 Mint
- **Eevee ex** (167/131) - CAPY 8.5 NM-M+

#### Shadow of the Blue Sea (Chinês)
- **Vaporeon** (#003/008) - CAPY 10 Gem Mint
- **Flareon** (#002/008) - CAPY 9 Mint
- **Jolteon** (#005/008) - CAPY 10 Gem Mint

#### Coroa Estelar
- **Lileep** (145/142) - CAPY 10 Gem Mint

#### Outras Raras
- **Mew Ancestral** (IP/∞) - Manafix 3 HP
- **Mewtwo** (SVP 052) - GBA 8 NM
- **Pikachu Shiny Chinese** (0706/09) - GBA 9 Mint

---

## 🛠️ Tecnologias Utilizadas

<div align="center">

| Tecnologia | Versão | Uso |
|------------|--------|-----|
| HTML5 | - | Estrutura das páginas |
| CSS3 | - | Estilização customizada |
| Bootstrap | 5.3.0 | Framework CSS responsivo |
| JavaScript | - | Interatividade (modals, collapse) |
| Cloudinary | - | Hospedagem de imagens |
| GitHub Pages | - | Deploy e hospedagem |

</div>

---

## 📁 Estrutura do Projeto

```
pericia_cartas/
│
├── index.html                          # Página principal do portfólio
├── README.md                           # Este arquivo
│
├── pages/                              # Páginas de laudo individuais
│   ├── pikachu-gold.html
│   ├── eevee-ex-evol-prism-c001090.html
│   ├── lileep-coroa-estelar-145-capy-10.html
│   ├── vaporeon-shadow-blue-sea-c001088.html
│   ├── flareon-shadow-blue-sea-c001087.html
│   ├── jolteon-shadow-blue-sea-c001089.html
│   └── ...
│
├── .claude/                            # Configurações do Claude Code
│   └── skills/
│       └── pericia-template/           # Skill para criação de laudos
│           ├── skill.md
│           ├── reference.md
│           └── template_pericia.html
│
└── template_pericia.html               # Template base para novos laudos
```

---

## 🚀 Como Usar

### Visualizar o Portfólio

Acesse o portfólio online: [https://afonsolelis.github.io/laudo_cards/](https://afonsolelis.github.io/laudo_cards/)

### Executar Localmente

```bash
# Clone o repositório
git clone https://github.com/afonsolelis/laudo_cards.git

# Entre no diretório
cd laudo_cards

# Abra o index.html no navegador
# Ou use um servidor local (ex: Live Server no VS Code)
```

### Criar Novo Laudo

1. Use o template `template_pericia.html` como base
2. Substitua todas as variáveis `{{VARIAVEL}}` pelos dados da carta
3. Salve em `pages/nome-da-carta.html`
4. Adicione o card no `index.html`
5. Faça commit e push das alterações

Ou use a skill do Claude Code:
```bash
/pericia-template
```

---

## 📖 Estrutura de um Laudo

Cada laudo técnico contém:

### 1. Identificação
- Nome da carta e número
- Coleção e ano de lançamento
- Raridade e tipo
- Idioma e fabricante
- Ilustrador/artista

### 2. Graduação
- Graduadora e certificado
- Nota final e descrição
- Data da certificação
- Ranking de população
- Link para laudo oficial

### 3. Análise de Condição
- Descrição da escala de graduação
- Nota geral com barra de progresso
- Análise por componente:
  - **Centering** (Centralização)
  - **Corners** (Cantos)
  - **Edges** (Bordas)
  - **Surface** (Superfície)
- Observações técnicas detalhadas
- Verificação de autenticidade

### 4. Histórico e Contexto
- Timeline de eventos importantes
- Informações sobre o ilustrador
- Notas sobre a graduadora
- Observações importantes

### 5. Links de Referência
- TCGPlayer
- Price Charting
- Liga Pokémon Brasil
- MyP Cards

---

## 🎨 Design e Acessibilidade

### Princípios de Design

- ✅ **Mobile First** - Desenvolvido priorizando dispositivos móveis
- ✅ **Contraste Adequado** - Cores escolhidas para boa legibilidade
- ✅ **Hierarquia Visual** - Organização clara de informações
- ✅ **Consistência** - Padrões visuais mantidos em todas as páginas
- ✅ **Performance** - Imagens otimizadas via Cloudinary

### Paleta de Cores

```css
/* Graduações */
Gem Mint 10:     #198754 (verde)
Mint 9-9.5:      #198754 (verde)
Near Mint 8-8.5: #ffc107 (amarelo)
< 8:             #6c757d (cinza)

/* Tema */
Fundo:           #f8f9fa (cinza claro)
Primário:        #212529 (preto)
Secundário:      #6c757d (cinza)
Destaque:        #0d6efd (azul)
```

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Se você tem sugestões para melhorar o projeto:

1. Faça um Fork do projeto
2. Crie uma Branch para sua Feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

---

## 📝 Roadmap

- [x] Criar template base de laudo
- [x] Implementar sistema de cards clicáveis no index
- [x] Adicionar suporte para múltiplas graduadoras
- [x] Integração com Cloudinary para imagens
- [x] Links de referência para marketplaces
- [x] Adicionar link do GitHub no navbar
- [ ] Sistema de busca e filtros
- [ ] Gráficos de estatísticas da coleção
- [ ] Modo escuro (dark mode)
- [ ] Exportar laudos em PDF
- [ ] Sistema de tags e categorias
- [ ] Página de estatísticas gerais

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

## 👤 Autor

**Afonso Brandão**

- GitHub: [@afonsolelis](https://github.com/afonsolelis)
- Portfólio: [afonsolelis.github.io/laudo_cards](https://afonsolelis.github.io/laudo_cards/)

---

## 🙏 Agradecimentos

- [Bootstrap](https://getbootstrap.com/) - Framework CSS
- [Cloudinary](https://cloudinary.com/) - Hospedagem de imagens
- [GitHub Pages](https://pages.github.com/) - Hospedagem do site
- [Claude Code](https://claude.com/claude-code) - Assistência no desenvolvimento
- Comunidade Pokémon TCG Brasil

---

## 📊 Graduadoras Suportadas

### GBA Grading
- Sistema de notas de 1-10
- Registro AAA para cartas autênticas premium
- Subgrades detalhados por componente

### Manafix (MGS)
- Sistema de notas com escala numérica
- Programas especiais de graduação
- Foco em cartas do mercado brasileiro

### CAPY Games
- Nova graduadora emergente
- Sistema de 1-10 com subgrades
- Especializada em cartas asiáticas

---

<div align="center">

**⭐ Se este projeto foi útil para você, considere dar uma estrela! ⭐**

Made with ❤️ by [Afonso Brandão](https://github.com/afonsolelis)

</div>
