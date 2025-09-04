from onebike_datetimes import onebike_datetimes

# Initialize a list for all the trip durations
onebike_durations = []

for trip in onebike_datetimes:
  # Create a timedelta object corresponding to the length of the trip
  trip_duration = trip['end'] - trip['start']
  
  # Get the total elapsed seconds in trip_duration
  trip_length_seconds = trip_duration.total_seconds()
  
  # Append the results to our list
  onebike_durations.append(trip_length_seconds)

'''
O código acima demonstra como calcular a duração de cada viagem em segundos, utilizando a biblioteca datetime do Python. Ele cria uma lista chamada onebike_durations, onde armazena a duração de cada viagem em segundos, calculando a diferença entre os horários de início e fim de cada viagem.
'''