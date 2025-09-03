from onebike_datetimes import onebike_datetimes

# Create dictionary to hold results
trip_counts = {'AM': 0, 'PM': 0}
  
# Loop over all trips
for trip in onebike_datetimes:
  # Check to see if the trip starts before noon
  if trip['start'].hour < 12:
    # Increment the counter for before noon
    trip_counts['AM'] += 1
  else:
    # Increment the counter for after noon
    trip_counts['PM'] += 1
  
print(trip_counts)

'''
O código acima demonstra como contar o número de viagens de bicicleta que começam antes e depois do meio-dia, usando um dicionário para armazenar os resultados. Ele mostra a contagem de viagens em duas categorias: 'AM' para viagens que começam antes do meio-dia e 'PM' para aquelas que começam depois. Essa abordagem permite uma análise simples do padrão de uso da bicicleta ao longo do dia.
'''