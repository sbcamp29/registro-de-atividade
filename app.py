
from flask import Flask, request

app = Flask(__name__)

estilo = """
<style>
    body {
        font-family: "Verdana", sans-serif;
        background-color: #f4f6f8;
        margin: 20;
        padding: 20px;
    }

    .pagina {
        min-height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .card {
        background-color: #bcd2ee;
        width: 420px;
        padding: 32px;
        border-radius: 10px;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12);
    }
</style>
"""

gamificacoes = [
    "Participou de evento",
    "Fez curso",
    "Ajudou em projeto",
    "Participou de reunião",
    "Realizou treinamento"
]

@app.route("/", methods=["GET", "POST"])
@app.route("/registrarAtividade", methods=["GET", "POST"])
def registrar_atividade():
    if request.method == "POST":
        gamificacao = request.form.get("gamificacao")
        descricao = request.form.get("descricao")

        print("Gamificação:", gamificacao)
        print("Descrição:", descricao)

        return """
        <h1>Atividade registrada com sucesso!</h1>

        <a href="/registrarAtividade">
            <button>Registrar outra atividade</button>
        </a>

        <a href="/statusAtividades">
            <button>Ver status das atividades</button>
        </a>
        """

    opcoes = ""

    for gamificacao in gamificacoes:
        opcoes = opcoes + f'<option value="{gamificacao}">{gamificacao}</option>'

    return f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>Registrar Atividade</title>
       {estilo}
    </head>
    <head>
    <meta charset="UTF-8">
    <title>Registrar Atividade</title>


    </style>
</head>
    <body>
     <div class="pagina">
        <div class="card">
        <div class="body">
        <h1>Registrar Atividade</h1>

        <form method="POST" action="/registrarAtividade">
            <label>Gamificação:</label>
            <select name="gamificacao" required>
                {opcoes}
            </select>

            <br><br>

            <label>Descrição:</label>
            <textarea name="descricao" required></textarea>

            <br><br>

            <button type="submit">Adicionar</button>
        </form>
    </body>
    </html>
    """


@app.route("/statusAtividades")
def status_atividades():
    return "<h1>Página statusAtividades ainda será feita.</h1>"


if __name__ == "__main__":
    app.run(debug=True)


