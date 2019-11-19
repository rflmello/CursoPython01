from flask_mysqldb import MySQLdb
from cliente import Cliente

conexao = MySQLdb.connect(host='mysql.zuplae.com', user='zuplae04',passwd='lendas19',database='zuplae04')
cur = conexao.cursor()

cur.execute('SELECT ID, NOME, CPF, DATA_NASCIMENTO FROM Cliente')
lista_resultado = cur.fetchall()
lista_clientes = []
for c in lista_resultado:
    cliente = Cliente(c[0], c[1], c[2], c[3] )
    lista_clientes.append(cliente)
    print(cliente.__dict__)