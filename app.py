from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Servidor Flask Rodando com Sucesso!"

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        telefone = request.form.get('telefone')
        
        print(f"Dados Recebidos do HTML: Nome={nome}, Email={email}, Telefone={telefone}")
    
        return "Dados recebidos e processados com sucesso."    
    
    return render_template('form004.html')


@app.route('/formulario-esporte', methods=['GET', 'POST'])
def formulario_esporte():
    if request.method == 'POST':
        sexo_escolhido = request.form.get('sexo')
        basquete = request.form.get('esbas')
        futebol = request.form.get('esfut')
        natacao = request.form.get('esnat')
        tenis = request.form.get('esten')
        
        print(f"Dandos recebidos do Html: Sexo = {sexo_escolhido}, Basquete={basquete}, Futebol={futebol}, Natação={natacao}, Tenis={tenis}")
        
        return "Dados recebidos e processados com sucesso."
    return render_template('form005.html')
    

if __name__ == '__main__':
    app.run(debug=True)
