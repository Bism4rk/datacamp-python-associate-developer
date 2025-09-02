# Import the pandas package
import pandas as pd

# Initialize reader object: df_reader
df_reader = pd.read_csv('ind_pop.csv', chunksize=10)

# Print two chunks
print(next(df_reader))
print(next(df_reader))

'''
O código acima demonstra como usar o iterador `read_csv` do pandas para ler um arquivo CSV em pedaços menores. O arquivo 'ind_pop.csv' é lido em pedaços de 10 linhas, e os dois primeiros pedaços são impressos. Isso é útil para trabalhar com arquivos grandes que não cabem na memória de uma só vez, permitindo que você processe os dados em partes menores.
'''