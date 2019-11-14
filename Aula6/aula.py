from flask_mysqldb import MySQLdb

conexao = MySQL.connect(host='mysql.zuplae.com', user='zuplae04',passwd='lendas19',database='zupla04')
cur = conexao.cursos()

cur.execute('SELECT * FROM Cliente')

for c in cur.fetchall():
    print(c)