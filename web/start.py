from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return 'pagina principal em contrução 30/10'

@app.route('/cerveja')
def cerveja():
    return 'pagina secundária em contrução 30/10'

app.run()