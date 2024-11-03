import mysql.connector
import pandas as pd

# Conectar ao banco de dados
mydb = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="admin",
    password="admin",
    database="desafio"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM produtos_pedido INNER JOIN produtos ON produtos_pedido.produto_id = produtos.produto_id INNER JOIN pedidos ON produtos_pedido.pedido_id = pedidos.pedido_id INNER JOIN clientes ON pedidos.pedido_cliente = clientes.cliente_id")

myresult = mycursor.fetchall()
columns = [column[0] for column in mycursor.description]
df = pd.DataFrame(myresult, columns=columns)

mydb.close()

import matplotlib.pyplot as plt
import seaborn as sns

# Gráfico de barras: Produtos mais vendidos
sns.countplot(x='produto_nome', data=df)
plt.title('Produtos Mais Vendidos')
plt.xticks(rotation=45)
plt.show()

# Gráfico de barras: Clientes por estado
sns.countplot(x='cliente_estado', data=df)
plt.title('Clientes por Estado')
plt.show()

# Gráfico de dispersão: Quantidade de produtos vs. valor total do pedido (por pedido)
df['valor_total'] = df['quantidade'] * df['produto_valor']
sns.scatterplot(x='quantidade', y='valor_total', data=df)
plt.title('Quantidade de Produtos vs. Valor Total do Pedido')
plt.xlabel('Quantidade')
plt.ylabel('Valor Total')
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

# ... (seu código para criar o gráfico)

plt.legend(fontsize='small')  # ou 'medium', 'large', ou um valor numérico
plt.show()