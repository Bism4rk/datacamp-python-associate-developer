import pandas as pd

# Define count_entries()
def count_entries(csv_file, c_size, colname):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    
    # Initialize an empty dictionary: counts_dict
    counts_dict = {}

    # Iterate over the file chunk by chunk
    for chunk in pd.read_csv(csv_file, chunksize=c_size):

        # Iterate over the column in DataFrame
        for entry in chunk[colname]:
            if entry in counts_dict.keys():
                counts_dict[entry] += 1
            else:
                counts_dict[entry] = 1

    # Return counts_dict
    return counts_dict

# Call count_entries(): result_counts
result_counts = count_entries('tweets.csv', 10, 'lang')

# Print result_counts
print(result_counts)

'''
O código acima demonstra como usar iteradores para carregar arquivos grandes em pedaços menores, processando cada pedaço de dados separadamente. A função `count_entries` lê o arquivo 'tweets.csv' em pedaços de 10 linhas e conta as ocorrências de cada idioma, armazenando os resultados em um dicionário chamado `counts_dict`. Isso permite que você trabalhe com arquivos que não cabem na memória de uma só vez, evitando erros de memória e melhorando a eficiência do processamento.
'''