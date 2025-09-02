# Import date from datetime
from datetime import date

# Create a date object
hurricane_andrew = date(1992, 8, 24)

# Which day of the week is the date?
print(hurricane_andrew.weekday())

'''
O código acima demonstra como criar um objeto de data em Python e como determinar o dia da semana correspondente a essa data. A variável `hurricane_andrew` armazena a data do furacão Andrew, e o método `weekday()` retorna o dia da semana como um número inteiro, onde segunda-feira é 0 e domingo é 6. Nesse caso, o furacão Andrew ocorreu em uma segunda-feira.
'''