from flask import Flask, render_template

app = Flask(__name__)

projetos = [
    {
        "nome": "Sistema de Gerenciamento de Tarefas (To-Do List Avançado)",
        "descricao": "Um aplicativo web que permite aos usuários criar, editar e excluir tarefas, com funcionalidades adicionais como categorias, prazos e lembretes por e-mail.",
        "dificuldade": "3",
    },
    {
        "nome": "Sistema de Controle Financeiro Pessoal",
        "descricao": "Uma aplicação que ajuda os usuários a monitorar suas despesas e receitas, gerar relatórios financeiros e definir orçamentos mensais.",
        "dificuldade": "4",
    },
    {
        "nome": "Biblioteca Digital / Gerenciador de E-books",
        "descricao": "Um sistema que permite aos usuários organizar, buscar e gerenciar sua coleção digital de livros eletrônicos.",
        "dificuldade": "5",
    },
    {
        "nome": "API REST para Gerenciamento de Contatos",
        "descricao": "Uma API que permite aos usuários criar, ler, atualizar e excluir informações de contatos, com autenticação e autorização para proteger os dados.",
        "dificuldade": "6",
    },
    {
        "nome": "Sistema de Blog Simples com Comentários",
        "descricao": "Um aplicativo web onde os usuários podem criar postagens de blog, visualizar postagens de outros usuários e deixar comentários nas postagens.",
        "dificuldade": "6",
    },
    {
        "nome": "Scraper de Notícias com Armazenamento",
        "descricao": "Um script que coleta notícias de diferentes fontes online, armazena os dados em um banco de dados e exibe as notícias em uma interface web.",
        "dificuldade": "5",
    },
    {
        "nome": "Sistema de Inventário para Pequeno Negócio",
        "descricao": "Uma aplicação que ajuda os proprietários de pequenos negócios a gerenciar seu estoque, registrar vendas e gerar relatórios de inventário.",
        "dificuldade": "7",
    },
    {
        "nome": "Rastreador de Hábitos com Análise de Dados",
        "descricao": "Um aplicativo que permite aos usuários acompanhar seus hábitos diários, visualizar estatísticas e receber insights sobre seu comportamento ao longo do tempo.",
        "dificuldade": "5",
    },
    {
        "nome": "Sistema de Quiz/Flashcards com Repetição Espaçada",
        "descricao": "Um aplicativo que ajuda os usuários a aprender e memorizar informações usando o método de repetição espaçada, com suporte para criação de flashcards personalizados.",
        "dificuldade": "6",
    },
    {
        "nome": "Dashboard de Análise de Dados Pessoais (Integração com múltiplas fontes)",
        "descricao": "Um painel que integra dados de várias fontes (como fitness trackers, redes sociais, finanças pessoais) e apresenta visualizações e insights personalizados para o usuário.",
        "dificuldade": "7",
    },
]


@app.route("/")
def index():
    return render_template("index.html", projetos=projetos)


if __name__ == "__main__":
    app.run(debug=True)
