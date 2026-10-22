from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Servidor Flask Rodando com Sucesso!"

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        nome = request.form.get('nome')
        media = request.form.get('media')
        
        print(f"Dados Recebidos do HTML: Nome={nome}, Média={media}")
    
    
        return "Dados recebidos e processados com sucesso."    
    
    return render_template('form004.html')
if __name__ == '__main__':
    app.run(debug=True)
