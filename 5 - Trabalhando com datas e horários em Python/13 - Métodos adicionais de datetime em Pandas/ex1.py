import pandas as pd

rides = pd.read_csv('capital-onebike.csv', 
                    parse_dates = ['Start date', 'End date'])

# Localize the Start date column to America/New_York
rides['Start date'] = rides['Start date'].dt.tz_localize('America/New_York', 
                                						 ambiguous='NaT')

# Print first value
print(rides['Start date'].iloc[0])

# Convert the Start date column to Europe/London
rides['Start date'] = rides['Start date'].dt.tz_convert('Europe/London')

# Print the new value
print(rides['Start date'].iloc[0])

'''
O código acima demonstra como trabalhar com fusos horários em séries temporais usando a biblioteca Pandas em Python. Ele começa importando a biblioteca Pandas e lendo um arquivo CSV chamado 'capital-onebike.csv', que contém dados de viagens de bicicleta, incluindo colunas de datas de início e fim. As colunas de datas são analisadas como objetos datetime graças ao parâmetro `parse_dates`.
'''