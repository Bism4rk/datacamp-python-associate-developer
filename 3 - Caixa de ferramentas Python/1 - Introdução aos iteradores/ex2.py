# Create a list of strings: flash
flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']

# Print each list item in flash using a for loop
for person in flash:
    print(person)


# Create an iterator for flash: superhero
superhero = iter(flash)

# Print each item from the iterator
print(next(superhero))
print(next(superhero))
print(next(superhero))
print(next(superhero))

'''
O código acima demonstra como criar e usar um iterador em Python. Primeiro, uma lista de strings chamada `flash` é criada, contendo nomes de personagens. Em seguida, um loop `for` é usado para imprimir cada item da lista. Depois, a função `iter()` é chamada para criar um iterador a partir da lista `flash`, e a função `next()` é usada para acessar cada item do iterador sequencialmente. Isso mostra como os iteradores permitem percorrer coleções de dados de maneira eficiente.
'''