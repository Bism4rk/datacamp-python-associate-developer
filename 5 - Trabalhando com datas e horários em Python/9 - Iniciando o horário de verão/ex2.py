# Import datetime and tz
from datetime import datetime
from dateutil import tz

# Create starting date
dt = datetime(2000, 3, 29, tzinfo = tz.gettz('Europe/London'))

# Loop over the dates, replacing the year, and print the ISO timestamp
for y in range(2000, 2011):
  print(dt.replace(year=y).isoformat())

'''
O código acima demonstra como manipular datas e horários em Python, especificamente como lidar com anos bissextos. Primeiro, importamos a classe datetime do módulo datetime e o módulo tz da biblioteca dateutil. Em seguida, criamos um objeto datetime representando o dia 29 de março de 2000 no fuso horário de Londres (Europe/London). Utilizamos um loop para iterar sobre os anos de 2000 a 2010, substituindo o ano do objeto datetime original por cada ano do loop usando o método replace(). Finalmente, imprimimos cada data resultante no formato ISO 8601 usando o método isoformat().
'''