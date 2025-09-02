# Create an empty list
my_list = []

# Check the truthiness of my_list
print(bool(my_list))

# Append the string 'cookies' to my_list
my_list.append('cookies')

# Check the truthiness of my_list
print(bool(my_list))

'''
O código acima demonstra como booleanos em Python podem ser usados para verificar a "verdade" de um elemento, nesse caso uma lista. Inicialmente, a lista está vazia, o que resulta em `False` quando convertida para booleano. Após adicionar um elemento à lista, ela se torna não vazia, resultando em `True` quando convertida para booleano. Geralmente, elementos ou estruturas de dados vazias são considerados `False`, enquanto aqueles que contêm valores são considerados `True`.
'''