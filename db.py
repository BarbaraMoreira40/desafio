import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="admin",
    password="admin",
    database="desafio"
)

cursor = db.cursor()

sql = """
SELECT COUNT(DISTINCT c.cliente_id) AS total_clientes
FROM clientes c
INNER JOIN pedidos p ON c.cliente_id = p.pedido_cliente
"""

cursor.execute(sql)

# Obtém o resultado da consulta e imprime
resultado = cursor.fetchone()
total_clientes = resultado[0]
print("Total de Clientes:", total_clientes)

db.close()

