# Import datetime
from datetime import datetime

# Starting timestamps
timestamps = [1514665153, 1514664543]

# Datetime objects
dts = []

# Loop
for ts in timestamps:
  dts.append(datetime.fromtimestamp(ts))
  
# Print results
print(dts)

'''
O código acima demonstra como converter timestamps em objetos datetime. Ele faz um loop sobre todos os timestamps e usa a função fromtimestamp() para criar objetos datetime a partir deles.
'''