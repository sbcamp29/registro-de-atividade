
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


from banco import supabase

from flask import Flask, request, redirect, render_template
from banco import supabase

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <title>Registrar Gamificação</title>
    </head>
    <body>
        <h1>Registrar Gamificação</h1>
<form action="/registrar" method="POST">

    <input type="text" name="id_user" placeholder="ID do usuário" required>

    <textarea name="descricao" placeholder="Descrição"></textarea>

    <input type="number" step="0.01" name="frequencia" placeholder="Frequência">

    <input type="number" name="pontos" placeholder="Pontos">

    <input type="text" name="status" placeholder="Status">

    <button type="submit">Registrar</button>
</form>
    </body>
    </html>
    """

@app.post("/registrar")
def registrar():
    id_user = request.form.get("id_user")
    descricao = request.form.get("descricao")
    frequencia = request.form.get("frequencia")
    pontos = request.form.get("pontos")
    status = request.form.get("status")

    supabase.table("gamificacoes_registradas").insert({
        "id_user": id_user,
        "descricao": descricao,
        "frequencia": float(frequencia),
        "pontos": int(pontos),
        "status": status
    }).execute()

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)