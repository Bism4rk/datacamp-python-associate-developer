# Create a list of strings: lannister
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

# Create a generator object: lengths
lengths = (len(person) for person in lannister)

# Iterate over and print the values in lengths
for value in lengths:
    print(value)

'''
O código acima demonstra como criar um gerador que produz o comprimento dos nomes dos membros da família Lannister. Ele itera sobre o gerador e imprime cada comprimento. Geradores são úteis para economizar memória, pois produzem valores sob demanda, em vez de armazenar todos os valores na memória de uma só vez como compreensões de listas.
'''