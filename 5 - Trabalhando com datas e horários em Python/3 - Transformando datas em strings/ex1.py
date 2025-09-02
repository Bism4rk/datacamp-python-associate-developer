from datetime import date
from florida_hurricane_dates import florida_hurricane_dates

# Assign the earliest date to first_date
first_date = sorted(florida_hurricane_dates)[0]

# Convert to ISO and US formats
iso = "Our earliest hurricane date: " + first_date.isoformat()
us = "Our earliest hurricane date: " + first_date.strftime("%m/%d/%Y")

print("ISO: " + iso)
print("US: " + us)

'''
O código acima demonstra como trabalhar com datas em Python, convertendo uma data para diferentes formatos de string. Nesse caso, a data mais antiga de furacão da Flórida é convertida para os formatos ISO e US (YYYY-MM-DD e MM/DD/YYYY).
'''