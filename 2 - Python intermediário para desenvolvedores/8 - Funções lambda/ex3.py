sales_prices = [29.99, 9.95, 14.50, 39.75, 60.00]

# Create add_taxes to add 20% to each item in sales_prices
add_taxes = map(lambda x: x * 1.2, sales_prices)

# Create the updated list, sales_plus_tax
sales_plus_tax = list(add_taxes)

# Print the new list with updated values
print(sales_plus_tax)

'''
O código acima demonstra como usar a função `map` com uma função lambda para aplicar uma operação a cada item de uma lista. A função lambda é definida para calcular o preço com imposto, multiplicando cada preço de venda por 1.2. A função `map` aplica essa operação a todos os itens da lista `sales_prices`, e o resultado é convertido em uma lista chamada `sales_plus_tax`, que é então impressa. Funções lambda são úteis para criar funções pequenas e anônimas de forma concisa, especialmente quando usadas com funções como `map`, `filter` e `reduce`.
'''