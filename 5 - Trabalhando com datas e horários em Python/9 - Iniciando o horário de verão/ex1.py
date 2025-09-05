# Import datetime, timedelta, tz, timezone
from datetime import datetime, timedelta, timezone
from dateutil import tz

# Start on March 12, 2017, midnight, then add 6 hours
start = datetime(2017, 3, 12, tzinfo = tz.gettz('America/New_York'))
end = start + timedelta(hours=6)
print(start.isoformat() + " to " + end.isoformat())

# How many hours have elapsed?
print((end - start).total_seconds()/(60*60))

# What if we move to UTC?
print((end.astimezone(timezone.utc) - start.astimezone(timezone.utc))\
      .total_seconds()/(60*60))

'''
O código acima demonstra como lidar com datas e horários em Python, especialmente em relação ao horário de verão. Primeiro, importamos as classes necessárias do módulo datetime e o módulo tz da biblioteca dateutil. Em seguida, criamos um objeto datetime representando a meia-noite de 12 de março de 2017 no fuso horário de Nova York (America/New_York), que é quando o horário de verão começa. Adicionamos 6 horas a esse horário inicial para obter o horário final. Imprimimos ambos os horários no formato ISO 8601. Depois, calculamos e imprimimos a diferença em horas entre o horário inicial e final. Finalmente, convertendo ambos os horários para o fuso horário UTC, recalculamos a diferença em horas para mostrar que, devido ao início do horário de verão, a diferença real é menor do que 6 horas.
'''