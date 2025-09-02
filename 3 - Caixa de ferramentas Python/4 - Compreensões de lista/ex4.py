# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range(0, 5)] for row in range(0, 5)]

# Print the matrix
for row in matrix:
    print(row)

'''
O código acima demonstra como criar uma matriz 5 x 5 usando compreensões de lista em Python. A matriz é representada como uma lista de listas, onde cada sublista representa uma linha da matriz. A compreensão de lista permite gerar rapidamente as linhas e colunas da matriz, resultando em um código conciso e legível.

A compreensão de lista é composta por duas partes: a primeira parte define o valor de cada coluna (`col for col in range(0, 5)`) e a segunda parte define quantas vezes essa linha deve ser repetida (`for row in range(0, 5)`). O resultado é uma matriz onde cada linha contém os números de 0 a 4.
'''