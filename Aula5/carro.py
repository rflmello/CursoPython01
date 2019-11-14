class Carro:
    def __init__(self, marca='', modelo='', categoria='', ano=0):
        self.marca = marca
        self.modelo = modelo
        self.categoria = categoria
        self.ano = ano

    def lista_todos(self):
        lista_carros = []
        with open('Aula5/veiculos.txt','r') as arquivo:

            for c in arquivo:
                cl = c.strip().split(';')
                carro = Carro(cl[0], cl[1], cl[2], cl[3])
                lista_carros.append(carro)
        return lista_carros

#---Método para cadastro em arquivo texto

    def cadastrar(self):
        with open('Aula5/veiculos.txt','a') as arq :
            #--- Ao gravar a linha no arquivo texto f'{self}\n' , o self, o que é a própria classe
            #--- é convertida em string e ao ser convertida, é chamado o método __str__declarado abaixo
            arq.write(f'{self}\n')

#---Método de conversão da classe para string
#---Sempre que a classe for convertida para string (str()) este método será chamado
    def __str__(self):
        return f'{self.marca};{self.modelo};{self.categoria};{self.ano}'
