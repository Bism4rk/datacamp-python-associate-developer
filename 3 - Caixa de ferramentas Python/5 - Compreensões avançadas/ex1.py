# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [member for member in fellowship if len(member) >= 7]

# Print the new list
print(new_fellowship)

'''
O código acima demonstra como usar condicionais em compreensões de listas para filtrar elementos com base em um critério específico. Neste caso, ele cria uma nova lista contendo apenas os membros da 'fellowship' cujo nome tem 7 ou mais caracteres. A saída será:
['samwise', 'aragorn', 'legolas', 'boromir']
'''