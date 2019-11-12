#print('Digite o seu nome:')
#nome = input('Digite seu nome: ')
#print(nome)

from pessoa import Pessoa
from endereco import Endereco

print('='*50)
print('\n'*3)


pessoa = Pessoa()
print( pessoa.cadastrar_pessoa() )

endereco = Endereco()
print( endereco.cadastrar_endereco() )

print(pessoa.nome)
print(endereco.logradouro)



print('\n'*3)
print('='*50)

#print(f'Nome: {nome} Sobrenome: {sobrenome} Data de Nascimento: {data_nascimento} E-mail: {email} Senha: {senha}')