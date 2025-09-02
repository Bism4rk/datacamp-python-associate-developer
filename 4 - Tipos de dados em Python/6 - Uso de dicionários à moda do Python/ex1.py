squirrels_by_park = {'Madison Square Park': [{'primary_fur_color': 'Gray', 'highlights_in_fur_color': None, 'activities': 'Foraging', 'interactions_with_humans': 'Indifferent'}, {'primary_fur_color': 'Gray', 'highlights_in_fur_color': None, 'activities': 'Sitting', 'interactions_with_humans': 'Indifferent'}], 'Union Square Park': [{'primary_fur_color': 'Gray', 'highlights_in_fur_color': None, 'activities': 'Eating, Foraging', 'interactions_with_humans': None}, {'primary_fur_color': 'Cinnamon', 'highlights_in_fur_color': None, 'activities': 'Foraging', 'interactions_with_humans': None}, {'primary_fur_color': 'Gray', 'highlights_in_fur_color': None, 'activities': 'Eating, Foraging', 'interactions_with_humans': None}, {'primary_fur_color': 'Gray', 'highlights_in_fur_color': None, 'activities': 'Digging', 'interactions_with_humans': 'Indifferent'}]}

# Iterate over the first squirrel entry in the Madison Square Park list
for field, value in squirrels_by_park["Madison Square Park"][0].items():
    # Print field and value
    print(field, value)

print('-' * 13)

# Iterate over the second squirrel entry in the Union Square Park list
for field, value in squirrels_by_park["Union Square Park"][1].items():
    # Print field and value
    print(field, value)

'''
O código acima demonstra como iterar sobre os dicionários aninhados dentro de uma lista em um dicionário maior em Python. Os dois loops `for` percorrem os campos e valores dos dicionários de esquilos em dois parques diferentes, imprimindo cada campo e seu respectivo valor. A linha de separação é impressa entre as duas iterações para melhor visualização.
'''