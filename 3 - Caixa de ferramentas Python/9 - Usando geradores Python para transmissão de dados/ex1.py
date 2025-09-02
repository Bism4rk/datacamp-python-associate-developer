# Open a connection to the file
with open('world_dev_ind.csv') as file:

    # Skip the column names
    file.readline()

    # Initialize an empty dictionary: counts_dict
    counts_dict = {}

    # Process only the first 1000 rows
    for j in range(0, 1000):

        # Split the current line into a list: line
        line = file.readline().split(',')

        # Get the value for the first column: first_col
        first_col = line[0]

        # If the column value is in the dict, increment its value
        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1

        # Else, add to the dict and set value to 1
        else:
            counts_dict[first_col] = 1

# Print the resulting dictionary
print(counts_dict)

'''
O código acima demonstra como ler um arquivo CSV, pular a primeira linha (que contém os nomes das colunas) e contar a ocorrência de valores na primeira coluna do arquivo. Ele:
- Abre o arquivo `world_dev_ind.csv`.
- Lê a primeira linha para ignorar os nomes das colunas.
- Inicializa um dicionário vazio `counts_dict` para armazenar as contagens.
- Processa as primeiras 1000 linhas do arquivo, dividindo cada linha em uma lista.
- Verifica se o valor da primeira coluna já está no dicionário. Se estiver, incrementa o contador; caso contrário, adiciona o valor ao dicionário com um contador inicial de 1.
- Por fim, imprime o dicionário resultante, que contém os valores únicos da primeira coluna como chaves e suas respectivas contagens como valores.
'''