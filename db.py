import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    port = 3306,
    user="admin",
    password="admin",
    database = "desafio"
)
cursor = db.cursor()
sql='''
SELECT c.*,produtos.produto_nome,produtos.produto_desc,produtos.produto_valor FROM clientes AS c
INNER JOIN pedidos AS p ON c.cliente_id = p.pedido_cliente
INNER JOIN produtos_pedido AS pp ON p.pedido_id = pp.pedido_id
INNER JOIN produtos ON pp.produto_id = produtos.produto_id
'''
cursor.execute(sql)
clientes = cursor.fetchall()
print(clientes)
db.close()