from dateutil import tz
from onebike_datetimes import onebike_datetimes

# Create the timezone object
uk = tz.gettz('Europe/London')

# Pull out the start of the first trip
local = onebike_datetimes[0]['start']

# What time was it in the UK?
notlocal = local.astimezone(uk)

# Print them out and see the difference
print(local.isoformat())
print(notlocal.isoformat())

# Create the timezone object
ist = tz.gettz('Asia/Kolkata')

# Pull out the start of the first trip
local = onebike_datetimes[0]['start']

# What time was it in India?
notlocal = local.astimezone(ist)

# Print them out and see the difference
print(local.isoformat())
print(notlocal.isoformat())

# Create the timezone object
sm = tz.gettz('Pacific/Apia')

# Pull out the start of the first trip
local = onebike_datetimes[0]['start']

# What time was it in Samoa?
notlocal = local.astimezone(sm)

# Print them out and see the difference
print(local.isoformat())
print(notlocal.isoformat())

'''
O código acima demonstra como converter datas e horas entre diferentes fusos horários usando a biblioteca dateutil em Python. Primeiro, importamos o módulo tz da biblioteca dateutil e os dados de datetime do arquivo onebike_datetimes. Em seguida, criamos objetos de fuso horário para Londres (Reino Unido), Kolkata (Índia) e Apia (Samoa) usando tz.gettz(). Para cada fuso horário, extraímos o início da primeira viagem em onebike_datetimes e usamos o método astimezone() para converter essa data e hora para o fuso horário correspondente. Finalmente, imprimimos tanto a data e hora original quanto a convertida em formato ISO 8601 para observar as diferenças.
'''