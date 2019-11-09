from flask import Flask, render_template, request

nome_pagina = "Ambev"
app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html', nome_pagina = nome_pagina)

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html', nome_pagina = nome_pagina)

@app.route('/salvar')
def salvar():
    nome = request.args["Nome"]
    tipo = request.args["Tipo"]
    teor = request.args["Teor"]
    with open('cervejas.txt','a') as arq :
        arq.write(f'{nome};{tipo};{teor}')
    return 'salvo '

app.run(debug=True)