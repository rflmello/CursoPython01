def cadastrar_endereco():
    logradouro = input('Informe o logradouro: ')
    numero = input('Informe o número de endereço: ')
    complemento = input('Informe o complemento: ')
    bairro = input('Informe o bairro: ')
    cidade = input('Informe a cidade: ')
    cep = input('Informe o CEP: ')
    return f'Logradouro: {logradouro} Número de endereço: {numero} Complemento: {complemento} Bairro: {bairro} Cidade: {cidade} CEP: {cep}'