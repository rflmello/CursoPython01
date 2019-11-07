class Aluno:
    
    nome = ''
    sobrenome = ''
    usuario = ''
    senha = ''

    def cadastrar_aluno(self):
        self.nome = input('Digite seu nome: ')
        self.sobrenome = input('Digite seu sobrenome: ')
        self.usuario = input('Digite seu usuário: ')
        self.senha = input('Digite sua senha: ')
        return f'Nome: {self.nome} Sobrenome: {self.sobrenome} Usuário: {self.usuario} Senha: {self.senha}'

#class Aluno:
#    def __init__(self):
#        self.nome = ''
#        self.sobrenome = ''
#        self.usuario = ''
#        self.senha = ''
