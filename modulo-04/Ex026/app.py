from flask import Flask, request

app = Flask(__name__)


# Rota que mostra o formulário HTML na tela
@app.route("/")
def index():
  return """
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Formulário</title>
        <style>
            body { background-color: rgba(27, 24, 36, 0.57); font-family: Arial, sans-serif; color: white; padding: 30px; }
        </style>
    </head>
    <body>
        <h1>Teste de formulário</h1>
        <form action="/cadastro" method="post">
            <p>
                <label for="iusu">Usuário: </label>
                <input type="text" name="iusu" id="iusu">
            </p>
            <p>
                <label for="isen">Senha: </label>
                <input type="password" name="sen" id="isen">
            </p>
            <p>
                <input type="submit" value="Enviar">
                <input type="reset" value="Limpar">
            </p>
        </form>
    </body>
    </html>
    """


# Rota que recebe os dados quando você clica em "Enviar"
@app.route("/cadastro", methods=["POST"])
def cadastro():
  usuario = request.form.get("iusu")
  senha = request.form.get("sen")

  return f"""
    <div style="font-family: Arial; padding: 20px;">
        <h1>Os dados foram enviados.</h1>
        <p>Aprenda PHP para manipular dados (simulado com Python/Flask!).</p>
        <hr>
        <h3>Dados recebidos pelo servidor:</h3>
        <p><strong>Usuário:</strong> {usuario}</p>
        <p><strong>Senha:</strong> {senha}</p>
    </div>
    """


if __name__ == "__main__":
  app.run(debug=True, port=5000)