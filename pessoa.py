class Pessoa:
    
    def cadastrar_pessoa(self):
        nome = input('Digite seu nome: ')
        sobrenome = input('Digite seu sobrenome: ')
        data_nascimento = input('Digite sua data de nascimento: ')
        email = input('Digite seu e-mail: ')
        senha = input('Digite sua senha: ')
        return f'Nome: {nome} Sobrenome: {sobrenome} Data de Nascimento: {data_nascimento} E-mail: {email} Senha: {senha}'