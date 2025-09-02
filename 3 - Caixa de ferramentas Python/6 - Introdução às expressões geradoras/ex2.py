# Create generator object: result
result = (num for num in range(0, 31))

# Print the first 5 values
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))

# Print the rest of the values
for value in result:
    print(value)

'''
O código acima demonstra como criar um gerador que produz números de 0 a 30. Ele imprime os primeiros cinco valores usando a função `next()` e, em seguida, imprime os valores restantes em um loop. Geradores são úteis para economizar memória, pois produzem valores sob demanda, em vez de armazenar todos os valores na memória de uma só vez como compreensões de listas.
'''