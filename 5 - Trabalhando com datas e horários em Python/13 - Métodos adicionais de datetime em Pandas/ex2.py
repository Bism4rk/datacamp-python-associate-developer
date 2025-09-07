import pandas as pd
from ex1 import rides

# Add a column for the weekday of the start of the ride
rides['Ride start weekday'] = rides['Start date'].dt.day_name()

# Print the median trip time per weekday
print(rides.groupby('Ride start weekday')['Duration'].median())

'''
O código acima continua o trabalho com o DataFrame `rides` que foi previamente carregado e processado no arquivo `ex1.py`. Ele adiciona uma nova coluna chamada 'Ride start weekday', que contém o nome do dia da semana em que cada viagem começou, utilizando o método `dt.day_name()`. Em seguida, o código calcula e imprime a duração mediana das viagens agrupadas por dia da semana, utilizando o método `groupby()` seguido de `median()`. Isso permite analisar como a duração das viagens varia ao longo dos dias da semana.
'''