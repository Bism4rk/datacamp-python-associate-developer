from florida_hurricane_dates import florida_hurricane_dates

# A dictionary to count hurricanes per calendar month
hurricanes_each_month = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6:0,
		  				 7: 0, 8:0, 9:0, 10:0, 11:0, 12:0}

# Loop over all hurricanes
for hurricane in florida_hurricane_dates:
  # Pull out the month
  month = hurricane.month
  # Increment the count in your dictionary by one
  hurricanes_each_month[month] += 1
  
print(hurricanes_each_month)

'''
O código acima demonstra como contar quantos furacões ocorreram em cada mês do ano. Ele cria um dicionário para armazenar a contagem de furacões por mês e itera sobre a lista de datas de furacões, incrementando a contagem correspondente no dicionário. Por fim, ele imprime o dicionário com a contagem de furacões por mês.
'''