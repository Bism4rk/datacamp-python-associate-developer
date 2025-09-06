# Import pandas
import pandas as pd

# Load CSV into the rides variable
rides = pd.read_csv('capital-onebike.csv', 
                    parse_dates = ['Start date', 'End date'])

# Print the initial (0th) row
print(rides.iloc[0])

'''
O código acima demonstra como carregar um arquivo CSV contendo dados de viagens de bicicletas compartilhadas usando a biblioteca pandas em Python. Ele lê o arquivo 'capital-onebike.csv', converte as colunas 'Start date' e 'End date' em objetos datetime, e imprime a primeira linha do DataFrame resultante, que contém informações sobre a primeira viagem registrada.
'''