from flask import Flask, render_template
from aluno import Aluno
from avaliacao import Avaliacao

aluno1 = Aluno()
aluno1.nome = 'Rafael'
aluno1.sobrenome = 'Melo'
aluno1.usuario = 'rafael'
aluno1.senha = '123'

aluno2 = Aluno()
aluno2.nome = 'Nome2'
aluno2.sobrenome = 'Sobrenome2'
aluno2.usuario = 'nome2'
aluno2.senha = '123'

avaliacao1 = Avaliacao()
avaliacao1.data = '06/11/2019'
avaliacao1.nome_avaliacao = 'Python'
avaliacao1.nota = '8'

avaliacao2 = Avaliacao()
avaliacao2.data = '07/11/2019'
avaliacao2.nome_avaliacao = 'Java'
avaliacao2.nota = '6'

app = Flask(__name__)

nome_pagina = "Pagina Web Rafael"

lista = [aluno1, aluno2]
lista2 = [avaliacao1, avaliacao2]

@app.route('/')
def inicio():
    return render_template('home.html', nome = nome_pagina, lista = lista, lista2 = lista2)

@app.route('/contato')
def contato():
    return render_template('contato.html', nome = nome_pagina, lista2 = lista2)

app.run(debug=True)