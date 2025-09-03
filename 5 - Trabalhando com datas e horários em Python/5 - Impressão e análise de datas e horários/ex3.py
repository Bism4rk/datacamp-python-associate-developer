# Import datetime
from datetime import datetime
from onebike_datetimes import onebike_datetimes

# Pull out the start of the first trip
first_start = onebike_datetimes[0]['start']

# Format to feed to strftime()
fmt = "%Y-%m-%dT%H:%M:%S"

# Print out date with .isoformat(), then with .strftime() to compare
print(first_start.isoformat())
print(first_start.strftime(fmt))

'''
O código acima demonstra como formatar objetos datetime em strings. Ele usa o método isoformat() para obter uma representação padrão da data e hora, e o método strftime() para formatar a data e hora de acordo com um formato específico.
'''