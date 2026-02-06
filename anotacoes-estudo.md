# 📚 Anotações de Estudo - Desenvolvimento Web

> Referência rápida de conceitos aprendidos durante o desenvolvimento do portfólio

---

## 🔧 GIT & GITHUB

### Comandos Essenciais
- **`git init`** - Inicia repositório Git local na pasta atual
- **`git add .`** - Adiciona todos os arquivos modificados para staging area (preparação para commit)
- **`git commit -m "mensagem"`** - Salva snapshot do código com descrição
- **`git push`** - Envia commits locais para repositório remoto (GitHub)
- **`git remote add origin [url]`** - Conecta repositório local ao remoto

### Conceitos
- **`.gitignore`** - Arquivo que lista o que o Git NÃO deve versionar
  - Exemplos: `venv/`, `__pycache__/`, `*.pyc`
  
- **SSH vs HTTPS**
  - SSH: Usa chaves criptográficas (mais seguro, não pede senha)
  - HTTPS: Usa token/senha para autenticação
  
- **Personal Access Token** - Senha especial do GitHub para autenticação via HTTPS

### Boas Práticas - Versionamento
- ✅ **Commit frequente** - Cada funcionalidade completa = 1 commit
- ✅ **Mensagens claras** - Descreva O QUE mudou, não como
  - Bom: `"Adiciona seção de projetos"`
  - Ruim: `"mudei o código"`
- ✅ **Push regular** - Backup automático no GitHub

### Mensagens de Commit - Convenção
**Formato:** `tipo(escopo): descrição`

**Tipos comuns:**
- `feat` - Nova funcionalidade
- `fix` - Correção de bug
- `docs` - Documentação
- `style` - Formatação (não muda lógica)
- `refactor` - Refatoração de código

**Regras:**
- Use imperativo: "Adiciona", "Corrige", "Atualiza"
- Tamanho: 50-72 caracteres idealmente
- Commits atômicos: 1 commit = 1 mudança lógica

**Exemplos:**
```bash
feat(readme): adiciona documentação do projeto
fix(css): corrige overflow no mobile
docs(anotacoes): atualiza notas da sessão 2
```

---

## 📦 POETRY

### Comandos
- **`poetry init`** - Cria projeto Python com gerenciamento de dependências
- **`poetry add [pacote]`** - Instala biblioteca e registra no `pyproject.toml`
- **`poetry run [comando]`** - Executa comando dentro do ambiente virtual do Poetry

### Arquivos
- **`pyproject.toml`** - Define dependências e configurações do projeto
- **`poetry.lock`** - Versões exatas das dependências (não versionar)

---

## 🌐 FLASK - BÁSICO

### O que é
**Flask** - Framework web minimalista em Python para criar aplicações web

### Conceitos Fundamentais
- **`@app.route('/')`** - Decorador que define URL e função que responde
- **`render_template()`** - Processa arquivo HTML da pasta `templates/`
- **`app.run(debug=True)`** - Inicia servidor local
  - `debug=True` - Recarrega automaticamente ao salvar código

### Estrutura de Pastas
```
projeto/
├── app.py
├── templates/          # Pasta obrigatória para HTML
│   └── index.html
├── static/            # Arquivos estáticos (CSS, JS, imagens)
│   └── style.css
└── pyproject.toml
```

### Passagem de Dados
```python
# Enviar dados para template
render_template("index.html", variavel=valor)

# Múltiplas variáveis
render_template("index.html", nome="João", idade=25, projetos=lista)
```

---

## 🎨 JINJA2 - TEMPLATE ENGINE

### Sintaxe Básica
- **`{% %}`** - Lógica (loops, condicionais) - não imprime nada
- **`{{ }}`** - Expressões - imprime valor na página
- **`{# #}`** - Comentários - não aparece no HTML final

### Loops
```html
{% for item in lista %}
    <p>{{ item }}</p>
{% endfor %}
```

### Acessar Dicionários
```html
{{ dicionario.chave }}
<!-- Equivale a: dicionario["chave"] -->
```

### Arquivos Estáticos
```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
<img src="{{ url_for('static', filename='foto.jpg') }}">
```

---

## 🐍 PYTHON - ESTRUTURAS DE DADOS

### Lista `[ ]`
- Coleção **ordenada** de itens
- Acesso por índice: `lista[0]`, `lista[1]`
```python
frutas = ["maçã", "banana", "laranja"]
print(frutas[0])  # maçã
```

### Dicionário `{ }`
- Coleção de pares **chave:valor**
- Acesso por chave: `dicionario["chave"]`
```python
pessoa = {"nome": "João", "idade": 25}
print(pessoa["nome"])  # João
```

### Lista de Dicionários
Padrão comum para dados estruturados
```python
projetos = [
    {"nome": "Projeto 1", "dificuldade": 3},
    {"nome": "Projeto 2", "dificuldade": 5}
]
```

---

## 📄 HTML - ESTRUTURA

### Tags Essenciais
```html
<!DOCTYPE html>        <!-- Declara HTML5 -->
<meta charset="UTF-8"> <!-- Aceita acentos -->
<meta name="viewport" content="width=device-width, initial-scale=1.0">
                       <!-- Responsivo em mobile -->
```

### Estrutura Semântica
Usar tags com significado ao invés de apenas `<div>`
```html
<header>   <!-- Cabeçalho -->
<nav>      <!-- Navegação -->
<section>  <!-- Seção de conteúdo -->
<footer>   <!-- Rodapé -->
```

**Vantagem:** Melhor para SEO e acessibilidade

---

## 🎨 CSS - FUNDAMENTOS

### Reset CSS
```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
```
- Remove estilos padrão inconsistentes entre navegadores
- `box-sizing: border-box` - Inclui padding/border no width total

### Unidades
- **`px`** - Pixels (fixo)
- **`rem`** - Relativo ao tamanho da fonte raiz (melhor para acessibilidade)
- **`%`** - Porcentagem do elemento pai

### Centralização
```css
.container {
    max-width: 1200px;
    margin: 0 auto;  /* Centraliza horizontalmente */
}
```

### Pseudo-classes
```css
a:hover {
    color: blue;  /* Ao passar o mouse */
}
```

### Transições
```css
.card {
    transition: transform 0.3s;
}

.card:hover {
    transform: translateY(-5px);  /* Move 5px para cima */
}
```

---

## 📐 CSS - FLEXBOX

### O que é
Sistema de layout moderno para **alinhar elementos** em uma dimensão (linha ou coluna)

### Conceitos
```css
.container {
    display: flex;
    justify-content: space-between;  /* Distribui espaço */
    align-items: center;             /* Alinha verticalmente */
    gap: 2rem;                       /* Espaço entre items */
}
```

### Exemplo Prático
```css
/* Menu: logo à esquerda, links à direita */
nav {
    display: flex;
    justify-content: space-between;
}
```

---

## 🎯 CSS - GRID LAYOUT

### O que é
Sistema de layout **bidimensional** (linhas E colunas)

### Grid Responsivo
```css
.projetos-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
}
```

**Explicação:**
- `repeat(auto-fit, ...)` - Ajusta número de colunas automaticamente
- `minmax(300px, 1fr)` - Mínimo 300px, máximo 1 fração do espaço
- `1fr` - Unidade flexível (divide espaço igualmente)
- `gap` - Espaçamento entre items

**Resultado:** Cards se reorganizam conforme tamanho da tela (mobile-first!)

---

## 🎨 CSS - EFEITOS VISUAIS

### Cantos Arredondados
```css
border-radius: 8px;  /* Leve arredondamento */
border-radius: 50%;  /* Círculo perfeito */
```

### Sombras
```css
box-shadow: 0 5px 15px rgba(0,0,0,0.1);
/*          x  y  blur spread cor */
```

### Cores com Transparência
```css
rgba(0, 0, 0, 0.1)
/*   R  G  B  Alpha */
/* 0.1 = 10% opaco */
```

### Posicionamento Sticky
```css
header {
    position: sticky;
    top: 0;  /* Fica fixo ao rolar */
}
```

---

## ✅ CSS - BOAS PRÁTICAS

### Organização
```css
/* ========== SEÇÃO DE PROJETOS ========== */
#projetos {
    /* ... */
}
```
- Use comentários para separar seções

### Nomenclatura
- ✅ `.projeto-card` - Semântico, descritivo
- ❌ `.card-1` - Genérico, sem significado

### Mobile-First
- Grid com `auto-fit` é automaticamente responsivo
- Não precisa de media queries básicas

---

## 📝 MARKDOWN

### Sintaxe Básica
```markdown
# Título H1
## Título H2
### Título H3

**Negrito**
*Itálico*

- Lista
- Com itens

1. Lista
2. Numerada

[Link](https://exemplo.com)

` ``código` ``   (sem espaços)

- [ ] To-do list
- [x] Item concluído
```

### README - Estrutura Comum
1. Título do projeto
2. Descrição breve
3. Tecnologias usadas
4. Como instalar/rodar
5. Como usar
6. Autor
7. Licença (opcional)

### Dicas
- Emojis tornam README mais visual (📚 🚀 ✅)
- Use badges para status (opcional, avançado)

---

## 🎯 GESTÃO DE PROJETO

### Produtividade
- **Sessões de tempo** - Blocos definidos evitam burnout
- **Priorização** - Funcionalidade > Estética
- **MVP First** - Versão mínima funcional primeiro

### Aprendizado Iterativo
- **Feedback positivo** - Reconhecer acertos motiva
- **Sugestões > Correções** - "Poderia..." > "Está errado"
- **Prática deliberada** - Repetir até automatizar

### Organização
- **Consistência > Intensidade** - 1h/dia > 7h sábado
- **Documentar = Aprender** - Escrever fixa conhecimento
- **Review espaçado** - Rever após 1 dia, 1 semana, 1 mês

---

## 🚀 PRÓXIMOS PASSOS

- [ ] Deploy (Render, PythonAnywhere)
- [ ] Responsividade mobile
- [ ] Seção de contato
- [ ] Começar primeiro projeto (To-Do List)

---

_Última atualização: 06/02/2026_