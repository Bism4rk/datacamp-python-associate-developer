from datetime import timezone, timedelta
from onebike_datetimes import onebike_datetimes

# Create a timezone object corresponding to UTC-4
edt = timezone(timedelta(hours=-4))

# Loop over trips, updating the start and end datetimes to be in UTC-4
for trip in onebike_datetimes[:10]:
  # Update trip['start'] and trip['end']
  trip['start'] = trip['start'].replace(tzinfo=edt)
  trip['end'] = trip['end'].replace(tzinfo=edt)

'''
O código acima demonstra como trabalhar com fusos horários em Python, utilizando a biblioteca datetime. Ele cria um objeto timezone para representar o fuso horário UTC-4 e atualiza as datas de início e fim das viagens para refletir esse fuso horário.
'''