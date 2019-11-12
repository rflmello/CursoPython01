from flask import Flask, render_template, request

nome_pagina = "Ambev"
app = Flask(__name__)

@app.route('/')
def inicio():
    lista_cervejas = []
    with open('cervejas.txt','r') as arquivo:
        for l in arquivo:
            vetor = l.split(';')
            lista_cervejas.append(vetor)
            #nome = vetor [0]
            #nome = vetor [1]
            #nome = vetor [2]
    return render_template('index.html', nome_pagina = nome_pagina, lista = lista_cervejas)

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html', nome_pagina = nome_pagina)

@app.route('/salvar')
def salvar():
    nome = request.args["Nome"]
    tipo = request.args["Tipo"]
    teor = request.args["Teor"]
    with open('cervejas.txt','a') as arq :
        arq.write(f'{nome};{tipo};{teor}\n')
    return 'salvo '

app.run(debug=True)