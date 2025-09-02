# Import pandas as pd
import pandas as pd

sales = {
    'user-id': ["KM24", "JW59", "DS39", "PO02", "RS99", "WW12"],
    'date': ["2023-01-15", "2023-01-16", "2023-01-17", "2023-01-18", "2023-01-19", "2023-01-20"],
    'order-value': [150.00, 200.50, 99.99, 120.00, 300.00, 250.75]
}

# Convert sales to a pandas DataFrame
sales_df = pd.DataFrame(sales)

# Preview the first five rows
print(sales_df.head())

'''
O código acima demonstra como usar um pacote em Python. Nesse caso, o pacote utilizado é o pandas, que é amplamente usado para manipulação e análise de dados. O dicionário `sales` contém dados de vendas, incluindo IDs de usuários, datas e valores dos pedidos. Esses dados são convertidos em um DataFrame do pandas, que é uma estrutura de dados bidimensional semelhante a uma tabela. Em seguida, o método `head()` é usado para exibir as primeiras cinco linhas do DataFrame, permitindo uma rápida visualização dos dados.
'''