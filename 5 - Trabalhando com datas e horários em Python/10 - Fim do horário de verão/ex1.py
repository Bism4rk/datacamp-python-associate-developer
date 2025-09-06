from dateutil import tz
from onebike_datetimes import onebike_datetimes

# Loop over trips
for trip in onebike_datetimes:
  # Rides with ambiguous start
  if tz.datetime_ambiguous(trip['start']):
    print("Ambiguous start at " + str(trip['start']))
  # Rides with ambiguous end
  if tz.datetime_ambiguous(trip['end']):
    print("Ambiguous end at " + str(trip['end']))

'''
O código acima demonstra como identificar horários ambíguos em registros de viagens usando a biblioteca dateutil. Ele percorre uma lista de viagens, verificando se os horários de início ou fim são ambíguos devido a mudanças de horário, como o fim do horário de verão. Se um horário for ambíguo, ele imprime uma mensagem indicando o horário específico.
'''