from dataclasses import dataclass
from ex1 import WeightEntry
    
weight_log = [('Gentoo', 230.0, 5500.0, 'MALE'), ('Gentoo', 229.0, 5800.0, 'MALE'), ('Gentoo', 225.0, 5400.0, 'MALE'), ('Gentoo', 219.0, 5250.0, 'MALE'), ('Gentoo', 210.0, 4300.0, 'FEMALE'), ('Gentoo', 216.0, 4925.0, 'MALE')]

# Create the empty list: labeled_entries
labeled_entries = []

# Iterate over the weight_log entries
for species, flipper_length, body_mass, sex in weight_log:
    # Append a new WeightEntry instance to labeled_entries
    labeled_entries.append(WeightEntry(species, flipper_length, body_mass, sex))
    
# Print a list of the first 5 mass_to_flipper_length_ratio values
print([entry.mass_to_flipper_length_ratio for entry in labeled_entries[:5]])

'''
O código acima demonstra como usar uma dataclass em Python para armazenar e manipular dados. A classe `WeightEntry` é usada para representar entradas de peso de pinguins, com campos para a espécie, comprimento da nadadeira, massa corporal e sexo. O código cria uma lista chamada `labeled_entries`, onde cada entrada do log de peso é convertida em uma instância da dataclass `WeightEntry`. Em seguida, ele imprime a razão entre a massa corporal e o comprimento da nadadeira para as primeiras cinco entradas.
'''
