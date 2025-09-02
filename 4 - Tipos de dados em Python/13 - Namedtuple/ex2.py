from ex1 import SpeciesDetails, weight_log

labeled_entries = [SpeciesDetails(species=species, sex=sex, body_mass=body_mass) for species, sex, body_mass in weight_log]

# Iterate over the first twenty entries in labeled_entries
for entry in labeled_entries[:20]:
    # if the entry's species equals Chinstrap
    if entry.species == 'Chinstrap':
      # Print each entry's sex and body_mass seperated by a colon
      print(f'{entry.sex}:{entry.body_mass}')


'''
O código acima demontra como iterar sobre uma lista de namedtuples em Python. Ele usa uma list comprehension para criar uma lista chamada labeled_entries, onde cada entrada é uma instância de SpeciesDetails, preenchida com os dados de weight_log. Em seguida, ele itera sobre os primeiros vinte elementos dessa lista e verifica se o campo species é igual a 'Chinstrap'. Se for, ele imprime o campo sex e body_mass, separados por dois pontos.
'''