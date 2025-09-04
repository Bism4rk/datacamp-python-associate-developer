from ex1 import onebike_durations

# What was the total duration of all trips?
total_elapsed_time = sum(onebike_durations)

# What was the total number of trips?
number_of_trips = len(onebike_durations)
  
# Divide the total duration by the number of trips
print(total_elapsed_time / number_of_trips)

'''
O código acima demonstra como calcular a duração média das viagens de bicicleta, utilizando a lista onebike_durations. Ele soma todas as durações das viagens e divide pelo número total de viagens, resultando na duração média de uma viagem.
'''