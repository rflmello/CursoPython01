#print('Digite o seu nome:')
#nome = input('Digite seu nome: ')
#print(nome)

from pessoa import Pessoa
from endereco import cadastrar_endereco

print('='*50)
print('\n'*3)


pessoa = Pessoa()
print( pessoa.cadastrar_pessoa() )

endereco = cadastrar_endereco()
print(endereco)



print('\n'*3)
print('='*50)

#print(f'Nome: {nome} Sobrenome: {sobrenome} Data de Nascimento: {data_nascimento} E-mail: {email} Senha: {senha}')