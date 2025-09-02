records = [
    ['2014', 'F', '1', 'Emma'],
    ['2014', 'M', '2', 'Liam'],
    ['2014', 'F', '3', 'Olivia'],
    ['2014', 'M', '4', 'Noah'],
    ['2014', 'F', '5', 'Sophia']
]

# Create the list comprehension: baby_names
baby_names = [row[3] for row in records]
    
# Print the sorted baby names in ascending alphabetical order
print(sorted(baby_names))

'''
O código acima demonstra como usar compreensão de listas em Python para extrair nomes de bebês de uma lista de registros. Ele cria uma nova lista contendo apenas os nomes dos bebês e, em seguida, imprime essa lista ordenada em ordem alfabética ascendente.
'''