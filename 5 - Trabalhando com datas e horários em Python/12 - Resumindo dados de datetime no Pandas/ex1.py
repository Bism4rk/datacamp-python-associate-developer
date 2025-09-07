import pandas as pd

# Load CSV into the rides variable
rides = pd.read_csv('capital-onebike.csv', 
                    parse_dates = ['Start date', 'End date'])

# Create joyrides
joyrides = (rides['Start station'] == rides['End station'])

# Total number of joyrides
print("{} rides were joyrides".format(joyrides.sum()))

# Median of all rides
print("The median duration overall was {:.2f} seconds"\
      .format(rides['Duration'].median()))

# Median of joyrides
print("The median duration for joyrides was {:.2f} seconds"\
      .format(rides[joyrides]['Duration'].median()))

'''
O código acima demonstra como analisar dados de viagens de bicicletas compartilhadas usando a biblioteca pandas em Python. Ele carrega um arquivo CSV contendo informações sobre as viagens, identifica quais viagens foram "joyrides" (viagens que começaram e terminaram na mesma estação), e calcula tanto a duração mediana de todas as viagens quanto a duração mediana das "joyrides". Os resultados são então impressos no console.
'''