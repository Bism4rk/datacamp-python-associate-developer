from ex1 import rides

# Group rides by member type, and resample to the month
grouped = rides.groupby('Member type')\
  .resample('M', on='Start date')

# Print the median duration for each group
print(grouped['Duration'].median())

'''
O código acima demonstra como agrupar e resumir dados de viagens de bicicletas compartilhadas usando a biblioteca pandas em Python. Ele agrupa os dados pelo tipo de membro ('Member type') e reamostra os dados para uma base mensal com base na coluna 'Start date'. Em seguida, calcula a duração mediana das viagens para cada grupo e imprime os resultados no console.
'''