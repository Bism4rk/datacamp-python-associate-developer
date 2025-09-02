# Create a list of strings: mutants
mutants = ['charles xavier', 
            'bobby drake', 
            'kurt wagner', 
            'max eisenhardt', 
            'kitty pryde']

# Create a list of tuples: mutant_list
mutant_list = list(enumerate(mutants))

# Print the list of tuples
print(mutant_list)

# Unpack and print the tuple pairs
for index1, value1 in enumerate(mutants):
    print(index1, value1)

# Change the start index
for index2, value2 in enumerate(mutants, start=1):
    print(index2, value2)

'''
O código acima demonstra como usar a função `enumerate()` para criar uma lista de tuplas a partir de uma lista de strings. A função `enumerate()` atribui um índice a cada item da lista, criando pares de índice e valor. A lista resultante é impressa, e em seguida, um loop `for` é usado para desempacotar e imprimir os pares de índice e valor. O segundo loop mostra como alterar o índice inicial usando o parâmetro `start`, começando a contagem a partir de 1 em vez de 0.
'''