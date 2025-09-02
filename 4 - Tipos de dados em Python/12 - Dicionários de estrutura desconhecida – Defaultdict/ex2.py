# Import defaultdict
from collections import defaultdict

weight_log =  [('Gentoo', 'MALE', 5500.0), ('Chinstrap', 'MALE', 4300.0), ('Adlie', 'MALE', 3800.0), ('Gentoo', 'MALE', 5800.0), ('Chinstrap', 'MALE', 4100.0), ('Adlie', 'MALE', 3975.0), ('Gentoo', 'MALE', 5400.0), ('Chinstrap', 'MALE', 4800.0), ('Chinstrap', 'MALE', 3950.0), ('Gentoo', 'MALE', 5250.0), ('Gentoo', 'MALE', 4925.0), ('Adlie', 'MALE', 3950.0), ('Chinstrap', 'MALE', 3800.0), ('Chinstrap', 'MALE', 4050.0), ('Adlie', 'MALE', 3650.0)]


# Create a defaultdict with a default type of list: male_penguin_weights
male_penguin_weights = defaultdict(list)

# Iterate over the weight_log entries
for species, sex, body_mass in weight_log:
    # Use the species as the key, and append the body_mass to it
    male_penguin_weights[species].append(body_mass)
    
# Print the first 2 items of the male_penguin_weights dictionary
print(list(male_penguin_weights.items())[:2])

'''
O código acima demonstra como usar defaultdict para criar um dicionário em Python. A lista de tuplas `weight_log` contém informações sobre o peso de pinguins machos, onde cada tupla contém a espécie, o sexo e a massa corporal. O defaultdict é inicializado com uma lista como tipo padrão, permitindo que novas chaves sejam automaticamente criadas com uma lista vazia como valor. Durante a iteração sobre `weight_log`, os pesos são adicionados à lista correspondente à espécie no dicionário. Finalmente, os primeiros dois itens do dicionário são impressos.
'''