from ex1 import rides

# Resample rides to be monthly on the basis of Start date
monthly_rides = rides.resample('M', on='Start date')['Member type']

# Take the ratio of the .value_counts() over the total number of rides
print(monthly_rides.value_counts() / monthly_rides.size())

'''
O código acima demonstra como resumir dados de viagens de bicicletas compartilhadas usando a biblioteca pandas em Python. Ele reamostra os dados para uma base mensal com base na coluna 'Start date' e calcula a proporção de diferentes tipos de membros ('Member type') em relação ao total de viagens para cada mês. Os resultados são então impressos no console.
'''