from flask import Flask, render_template, request, redirect
from carro import Carro

nome_pagina = 'Carros'
app = Flask(__name__)

@app.route('/')
def inicio():
    lista_carros = []
    with open('Aula5/veiculos.txt','r') as arquivo:
        for l in arquivo:
            vetor = l.split(';')
            lista_carros.append(vetor)
    return render_template('index.html', nome_pagina = nome_pagina, lista = lista_carros)


@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html', nome_pagina = nome_pagina)

@app.route('/salvar')
def salvar():
    marca = request.args["marca"]
    modelo = request.args["modelo"]
    categoria = request.args["categoria"]
    ano = request.args["ano"]

    carro = Carro(marca, modelo, categoria, ano)
    with open('Aula5/veiculos.txt','a') as arq :
        arq.write(f'{carro.marca};{carro.modelo};{carro.categoria};{carro.ano}\n')
    return redirect('/')

app.run()