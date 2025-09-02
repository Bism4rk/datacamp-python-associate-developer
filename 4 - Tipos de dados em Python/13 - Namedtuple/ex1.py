# Import namedtuple from collections
from collections import namedtuple

weight_log = [('Gentoo', 'MALE', 5500.0), ('Chinstrap', 'MALE', 4300.0), ('Adlie', 'MALE', 3800.0), ('Gentoo', 'MALE', 5800.0), ('Chinstrap', 'MALE', 4100.0), ('Adlie', 'MALE', 3975.0), ('Gentoo', 'MALE', 5400.0), ('Chinstrap', 'MALE', 4800.0), ('Chinstrap', 'FEMALE', 3800.0), ('Adlie', 'FEMALE', 3450.0), ('Chinstrap', 'MALE', 3950.0), ('Gentoo', 'MALE', 5250.0), ('Gentoo', 'FEMALE', 4300.0), ('Gentoo', 'MALE', 4925.0), ('Adlie', 'FEMALE', 3550.0), ('Adlie', 'MALE', 3950.0), ('Chinstrap', 'MALE', 3800.0), ('Chinstrap', 'MALE', 4050.0), ('Adlie', 'MALE', 3650.0), ('Adlie', 'FEMALE', 3175.0)]


# Create the namedtuple: SpeciesDetails
SpeciesDetails = namedtuple('SpeciesDetails', ['species', 'sex', 'body_mass'])

# Create the empty list: labeled_entries
labeled_entries = []

# Iterate over the weight_log entries
for species, sex, body_mass in weight_log:
    # Append a new SpeciesDetails namedtuple instance for each entry to labeled_entries
    details = SpeciesDetails(species, sex, body_mass)
    labeled_entries.append(details)
    
print(labeled_entries[:5])

'''
O código acima demonstra como usar namedtuple para criar uma estrutura de dados mais legível e organizada. Ele define uma namedtuple chamada SpeciesDetails, que contém três campos: species, sex e body_mass. Então, ele itera sobre uma lista de tuplas chamada weight_log, criando uma instância de SpeciesDetails para cada entrada e adicionando-a a uma lista chamada labeled_entries. Finalmente, ele imprime os primeiros cinco elementos da lista labeled_entries. Isso torna os dados mais fáceis de entender e manipular, pois cada entrada agora é um objeto com campos nomeados em vez de uma tupla sem nome.
'''