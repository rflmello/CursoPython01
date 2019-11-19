from flask_mysqldb import MySQLdb
from cliente import Cliente

class ClienteDao:
    def lista_todos()
        conexao = MySQLdb.connect(host='mysql.zuplae.com', user='zuplae04',passwd='lendas19',database='zuplae04')
        cur = conexao.cursor()
        cur.execute('SELECT ID, NOME, CPF, DATA_NASCIMENTO FROM Cliente')
        lista_resultado = cur.fetchall()
        lista_clientes = []
        for c in lista_resultado:
            cliente = Cliente(c[1], c[2], c[3], [0])
            lista_clientes.append(cliente)
        return lista_clientes
    
    def buscar_por_id(self, id:int):
        conexao = MySQLdb.connect(host='mysql.zuplae.com', user='zuplae04',passwd='lendas19',database='zuplae04')
        cur = conexao.cursor()
        cur.execute(f'SELECT ID, NOME, CPF, DATA_NASCIMENTO FROM Cliente Where ID={id}')
        cur.fetone()
        cliente = Cliente(c[1], c[2], c[3], [0])
        return cliente

    def salvar(self, cliente:Cliente):
        conexao = MySQLdb.connect(host='mysql.zuplae.com', user='zuplae04',passwd='lendas19',database='zuplae04')
        cur = conexao.cursor()
        cur.execute(f'INSERT INTO Cliente (NOME, CPF, DATA_NASCIMENTO) VALUES( "{cliente.nome}", "{cliente.cpf}","{cliente.data_nascimento}")')
    
    def alterar(self, cliente:Cliente):
        conexao = MySQLdb.connect(host='mysql.zuplae.com', user='zuplae04',passwd='lendas19',database='zuplae04')
        cur = conexao.cursor()
        cur.execute(f'UPDATE Cliente set nome ="{cliente.nome}", CPF = "{cliente.cpf}, DATA_NASCIMENTO"{cliente.data_nascimento}" WHERE = ID ={cliente.id}')
    
    def deletar(self, id:int):
        conexao = MySQLdb.connect(host='mysql.zuplae.com', user='zuplae04',passwd='lendas19',database='zuplae04')
        cur = conexao.cursor()
        cur.execute(f'DELETE FROM Cliente WHERE ID={}')
        
