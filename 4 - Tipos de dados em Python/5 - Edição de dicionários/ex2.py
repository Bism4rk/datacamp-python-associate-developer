squirrels_by_park = {'Madison Square Park': [{'primary_fur_color': 'Gray', 'highlights_in_fur_color': None, 'activities': 'Foraging', 'interactions_with_humans': 'Indifferent'}, {'primary_fur_color': 'Gray', 'highlights_in_fur_color': None, 'activities': 'Sitting', 'interactions_with_humans': 'Indifferent'}], 'Tompkins Square Park': [{'primary_fur_color': 'Gray', 'highlights_in_fur_color': 'Gray', 'activities': 'Foraging', 'interactions_with_humans': 'Approaches'}, {'primary_fur_color': 'Gray', 'highlights_in_fur_color': 'Gray', 'activities': 'Climbing (down tree)', 'interactions_with_humans': 'Indifferent'}, {'primary_fur_color': 'Gray', 'highlights_in_fur_color': 'Gray', 'activities': 'Foraging', 'interactions_with_humans': 'Indifferent'}, {'primary_fur_color': 'Gray', 'highlights_in_fur_color': 'Gray', 'activities': 'Foraging', 'interactions_with_humans': 'Indifferent'}], 'Union Square Park': [{'primary_fur_color': 'Gray', 'highlights_in_fur_color': None, 'activities': 'Eating, Foraging', 'interactions_with_humans': None}, {'primary_fur_color': 'Cinnamon', 'highlights_in_fur_color': None, 'activities': 'Foraging', 'interactions_with_humans': None}, {'primary_fur_color': 'Gray', 'highlights_in_fur_color': None, 'activities': 'Eating, Foraging', 'interactions_with_humans': None}, {'primary_fur_color': 'Gray', 'highlights_in_fur_color': None, 'activities': 'Digging', 'interactions_with_humans': 'Indifferent'}]}

# Remove "Madison Square Park" from squirrels_by_park
squirrels_madison = squirrels_by_park.pop('Madison Square Park')

# Safely remove "City Hall Park" from squirrels_by_park with an empty dictionary as the default
squirrels_city_hall = squirrels_by_park.pop('City Hall Park', {})

# Delete "Union Square Park" from squirrels_by_park
del squirrels_by_park['Union Square Park']

# Print squirrels_by_park
print(squirrels_by_park)

'''
O código acima demonstra diferentes maneiras de remover chaves de um dicionário em Python. Ele utiliza o método `pop` para remover uma chave e retornar seu valor, enquanto o segundo uso de `pop` fornece um valor padrão vazio caso a chave não exista. O comando `del` é usado para remover uma chave sem retornar seu valor.
'''