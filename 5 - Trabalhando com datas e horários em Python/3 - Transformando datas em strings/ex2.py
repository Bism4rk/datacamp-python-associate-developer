# Import date
from datetime import date

# Create a date object
andrew = date(1992, 8, 26)

# Print the date in the format 'YYYY-MM'
print(andrew.strftime('%Y-%m'))

# Print the date in the format 'MONTH (YYYY)'
print(andrew.strftime('%B (%Y)'))

# Print the date in the format 'YYYY-DDD'
print(andrew.strftime('%Y-%j'))

'''
O código acima demonstra como trabalhar com objetos de data em Python, convertendo um objeto de data em diferentes formatos de string com o método strftime(). Nesse caso, a data de Andrew é convertida para os formatos 'YYYY-MM', 'MONTH (YYYY)' e 'YYYY-DDD' com os especificadores de formato correspondentes (%Y-%m, %B (%Y) e %Y-%j).
'''