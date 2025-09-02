girl_names = ['Emma', 'Olivia', 'Sophia', 'Ava', 'Isabella', 'Charlotte', 'Mia', 'Amelia', 'Harper', 'Evelyn']
boy_names = ['Liam', 'Noah', 'Oliver', 'Elijah', 'James', 'William', 'Benjamin', 'Lucas', 'Henry', 'Alexander']

# Pair up the girl and boy names: pairs
pairs = zip(girl_names, boy_names)

# Iterate over pairs
for rank, pair in enumerate(pairs):
    # Unpack pair: girl_name, boy_name
    girl_name, boy_name = pair
    # Print the rank and names associated with each rank
    print(f'Rank {rank+1}: {girl_name} and {boy_name}')


'''
O código acima demonstra como emparelhar listas usando a função `zip` em Python. Ele combina nomes de meninas e meninos em pares, e então itera sobre esses pares para imprimir o ranking e os nomes associados a cada classificação. A função `enumerate` é usada para obter o índice (ranking) de cada par.
'''