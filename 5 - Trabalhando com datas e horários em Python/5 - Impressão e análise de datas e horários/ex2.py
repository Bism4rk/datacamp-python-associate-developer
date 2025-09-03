from datetime import datetime
from onebike_dt_strings import onebike_datetime_strings

# Write down the format string
fmt = "%Y-%m-%d %H:%M:%S"

# Initialize a list for holding the pairs of datetime objects
onebike_datetimes = []

# Loop over all trips
for (start, end) in onebike_datetime_strings:
  trip = {'start': datetime.strptime(start, fmt),
          'end': datetime.strptime(end, fmt)}
  
  # Append the trip
  onebike_datetimes.append(trip)

'''
O código acima demonstra como converter strings de data e hora em objetos datetime. Ele faz um loop sobre todas as viagens e usa a função strptime() para analisar as strings de data e hora em objetos datetime.
'''