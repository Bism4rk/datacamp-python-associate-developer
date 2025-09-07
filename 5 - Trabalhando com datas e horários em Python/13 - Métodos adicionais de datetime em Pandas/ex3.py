from ex1 import rides
import datetime as dt

# Shift the index of the end date up one; now subract it from the start date
rides['Time since'] = rides['Start date'] - (rides['End date'].shift(1))

# Move from a timedelta to a number of seconds, which is easier to work with
rides['Time since'] = rides['Time since'].dt.total_seconds()

# Resample to the month
monthly = rides.resample('M', on='Start date')

# Print the average hours between rides each month
print(monthly['Time since'].mean()/(60*60))

'''
O código acima continua o trabalho com o DataFrame `rides` que foi previamente carregado e processado no arquivo `ex1.py`. Ele calcula o tempo decorrido entre o início de uma viagem e o término da viagem anterior, armazenando esse valor em uma nova coluna chamada 'Time since'. Para facilitar a análise, o tempo é convertido de um objeto timedelta para um número de segundos. Em seguida, os dados são reamostrados por mês usando o método `resample()`, e a média do tempo entre viagens é calculada e convertida para horas. Finalmente, o código imprime a média de horas entre viagens para cada mês.
'''