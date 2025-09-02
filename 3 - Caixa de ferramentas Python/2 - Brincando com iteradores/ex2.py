mutants = ['charles xavier', 
            'bobby drake', 
            'kurt wagner', 
            'max eisenhardt', 
            'kitty pryde']

aliases = ['professor x', 
            'iceman', 
            'nightcrawler', 
            'magneto', 
            'shadowcat']

powers = ['telepathy', 
          'cryokinesis', 
          'teleportation', 
          'magnetism', 
          'phasing']

# Create a list of tuples: mutant_data
mutant_data = list(zip(mutants, aliases, powers))

# Print the list of tuples
print(mutant_data)

# Create a zip object using the three lists: mutant_zip
mutant_zip = zip(mutants, aliases, powers)

# Print the zip object
print(mutant_zip)

# Unpack the zip object and print the tuple values
for value1, value2, value3 in mutant_zip:
    print(value1, value2, value3)

'''
O código acima demonstra como usar a função `zip()` para combinar várias listas em uma lista de tuplas. Três listas são criadas: `mutants`, `aliases` e `powers`. A função `zip()` é usada para criar um iterador que agrupa os elementos correspondentes das três listas em tuplas. A lista resultante de tuplas é impressa, e em seguida, um loop `for` é usado para desempacotar e imprimir os valores de cada tupla. Isso mostra como a função `zip()` pode ser útil para agrupar dados relacionados de diferentes coleções.
'''