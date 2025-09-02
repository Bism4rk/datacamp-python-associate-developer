import pandas as pd

# Initialize reader object: urb_pop_reader
urb_pop_reader = pd.read_csv('ind_pop_data.csv', chunksize=1000)

# Get the first DataFrame chunk: df_urb_pop
df_urb_pop = next(urb_pop_reader)

# Check out the head of the DataFrame
print(df_urb_pop.head())

# Check out specific country: df_pop_ceb
df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']

# Zip DataFrame columns of interest: pops
pops = zip(df_pop_ceb['Total Population'], df_pop_ceb['Urban population (% of total)'])

# Turn zip object into list: pops_list
pops_list = list(pops)

# Print pops_list
print(pops_list)

'''
O código acima demonstra como usar o iterador `read_csv` do pandas para ler um arquivo CSV em pedaços menores. O arquivo 'ind_pop_data.csv' é lido em pedaços de 1000 linhas, e o primeiro pedaço é armazenado em um DataFrame. Em seguida, filtramos os dados para obter informações sobre a população urbana de um país específico (neste caso, 'CEB'). Finalmente, combinamos as colunas de interesse em uma lista de tuplas, que contém a população total e a porcentagem da população urbana.
Isso é útil para trabalhar com arquivos grandes que não cabem na memória de uma só vez, permitindo que você processe os dados em partes menores e mais gerenciáveis.
'''