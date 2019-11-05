class Endereco:
    
    logradouro = ''
    numero = ''
    complemento = ''
    bairro = ''
    cidade = ''
    cep = ''

    def cadastrar_endereco(self):
        self.logradouro = input('Informe o logradouro: ')
        self.numero = input('Informe o número de endereço: ')
        self.complemento = input('Informe o complemento: ')
        self.bairro = input('Informe o bairro: ')
        self.cidade = input('Informe a cidade: ')
        self.cep = input('Informe o CEP: ')
        return f'Logradouro: {self.logradouro} Número de endereço: {self.numero} Complemento: {self.complemento} Bairro: {self.bairro} Cidade: {self.cidade} CEP: {self.cep}'