from florida_hurricane_dates import florida_hurricane_dates

# Counter for how many before June 1
early_hurricanes = 0

# We loop over the dates
for hurricane in florida_hurricane_dates:
  # Check if the month is before June (month number 6)
  if hurricane.month < 6:
    early_hurricanes = early_hurricanes + 1
    
print(early_hurricanes)

'''
O código acima demonstra como contar quantos furacões ocorreram na Flórida antes de 1º de junho. Ele itera sobre a lista de datas de furacões e verifica se o mês é anterior a junho, incrementando um contador sempre que essa condição é verdadeira.
'''