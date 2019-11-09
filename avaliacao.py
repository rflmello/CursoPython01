"""
class Avaliacao:
    
    data = ''
    nome_avaliacao = ''
    nota = ''
    
    def cadastrar_avaliacao(self):
        self.data = input('Digite a data da avaliação: ')
        self.nome_avaliacao = input('Digite o nome da avaliação: ')
        self.nota = input('Digite sua nota: ')
        return f'Data: {self.data} Nome avaliação: {self.nome_avaliacao} Nota: {self.nota}'
"""

class Avaliacao:
    def __init__(self, data, nome_avaliacao, nota):
        self.data = data
        self.nome_avaliacao = nome_avaliacao
        self.nota = nota

