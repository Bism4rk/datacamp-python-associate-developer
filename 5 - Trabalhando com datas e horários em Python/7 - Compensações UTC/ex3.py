from datetime import timezone
from onebike_datetimes import onebike_datetimes

# Loop over the trips
for trip in onebike_datetimes[:10]:
  # Pull out the start
  dt = trip['start']
  # Move dt to be in UTC
  dt = dt.astimezone(timezone.utc)
  
  # Print the start time in UTC
  print('Original:', trip['start'], '| UTC:', dt.isoformat())

'''
O código acima demonstra como converter horários de viagens para o fuso horário UTC em Python, utilizando a biblioteca datetime. Ele percorre as viagens, extrai a data de início e a converte para UTC, imprimindo o horário original e o horário convertido.
'''