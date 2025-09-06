from ex1 import rides

# Subtract the start date from the end date
ride_durations = rides['End date'] - rides['Start date']

# Convert the results to seconds
rides['Duration'] = ride_durations.dt.total_seconds

print(rides['Duration'].head())

'''
O código acima demonstra como calcular a duração das viagens de bicicletas compartilhadas usando a biblioteca pandas em Python. Ele subtrai a coluna 'Start date' da coluna 'End date' para obter a duração de cada viagem e, em seguida, converte essa duração para segundos, armazenando o resultado em uma nova coluna chamada 'Duration'. Finalmente, ele imprime os primeiros cinco valores da coluna 'Duration'.
'''