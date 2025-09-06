from dateutil import tz
from onebike_datetimes import onebike_datetimes

trip_durations = []
for trip in onebike_datetimes:
  # When the start is later than the end, set the fold to be 1
  if trip['start'] > trip['end']:
    trip['end'] = tz.enfold(trip['end'])
  # Convert to UTC
  start = trip['start'].astimezone(tz.UTC)
  end = trip['end'].astimezone(tz.UTC)

  # Subtract the difference
  trip_length_seconds = (end-start).total_seconds()
  trip_durations.append(trip_length_seconds)

# Take the shortest trip duration
print("Shortest trip: " + str(min(trip_durations)))

'''
O código acima demonstra como calcular a duração das viagens levando em consideração mudanças de horário, como o fim do horário de verão. Ele percorre uma lista de viagens, ajusta os horários finais ambíguos usando o atributo 'fold' e converte ambos os horários para UTC antes de calcular a duração da viagem. Finalmente, ele imprime a duração da viagem mais curta.
'''