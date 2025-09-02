import pandas as pd
import matplotlib.pyplot as plt # type: ignore

# Code from previous exercise
urb_pop_reader = pd.read_csv('ind_pop_data.csv', chunksize=1000)
df_urb_pop = next(urb_pop_reader)
df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']
pops = zip(df_pop_ceb['Total Population'], 
           df_pop_ceb['Urban population (% of total)'])
pops_list = list(pops)

# Use list comprehension to create new DataFrame column 'Total Urban Population'
df_pop_ceb['Total Urban Population'] = [int(pop[0] * pop[1] * 0.01) for pop in pops_list]

# Plot urban population data
df_pop_ceb.plot(kind='scatter', x='Year', y='Total Urban Population')
plt.show()

print(pops_list[0])

'''
O código acima demonstra como usar compreensão de listas para calcular a população urbana total a partir de um DataFrame do pandas. Ele lê os dados de um arquivo CSV em pedaços, filtra os dados para um código de país específico, e então calcula a população urbana total como uma nova coluna no DataFrame. Finalmente, ele plota os dados de população urbana ao longo dos anos e exibe o primeiro elemento da lista de populações urbanas.
'''