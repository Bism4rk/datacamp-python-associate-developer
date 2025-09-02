import pandas as pd

# Read in sales.csv
sales_df = pd.read_csv("C:\\Users\\reich\\Downloads\\python-programming-fundamentals-datacamp\\2 - Python intermediário para desenvolvedores\\3 - Pacotes\\stuff\\sales.csv")

# Print the mean order_value
print(sales_df["order_value"].mean())

# Print the total value of sales
print(sales_df["order_value"].sum())

print(sales_df)

'''
O código acima demonstra como usar o pacote pandas para ler um arquivo CSV e realizar operações básicas de análise de dados. O arquivo `sales.csv` contém dados de vendas, que são lidos em um DataFrame do pandas. Em seguida, o código calcula e imprime a média dos valores dos pedidos (`order_value`) e o valor total das vendas. Por fim, o DataFrame completo é impresso, permitindo uma visualização detalhada dos dados.
'''