squirrels_madison = [{'primary_fur_color': 'Gray', 'highlights_in_fur_color': None, 'activities': 'Sitting', 'interactions_with_humans': 'Indifferent'}, {'primary_fur_color': 'Gray', 'highlights_in_fur_color': 'Cinnamon', 'activities': 'Foraging', 'interactions_with_humans': 'Indifferent'}, {'primary_fur_color': 'Gray', 'highlights_in_fur_color': None, 'activities': 'Climbing, Foraging', 'interactions_with_humans': 'Indifferent'}]

squirrels_union = ('Union Square Park', [{'primary_fur_color': 'Gray', 'highlights_in_fur_color': None, 'activities': 'Eating, Foraging', 'interactions_with_humans': None}, {'primary_fur_color': 'Gray', 'highlights_in_fur_color': 'Cinnamon', 'activities': 'Climbing, Eating', 'interactions_with_humans': None}, {'primary_fur_color': 'Cinnamon', 'highlights_in_fur_color': None, 'activities': 'Foraging', 'interactions_with_humans': 'Indifferent'}, {'primary_fur_color': 'Gray', 'highlights_in_fur_color': None, 'activities': 'Running, Digging', 'interactions_with_humans': 'Runs From'}, {'primary_fur_color': 'Gray', 'highlights_in_fur_color': None, 'activities': 'Digging', 'interactions_with_humans': 'Indifferent'}, {'primary_fur_color': 'Gray', 'highlights_in_fur_color': 'Black', 'activities': 'Climbing', 'interactions_with_humans': None}, {'primary_fur_color': 'Gray', 'highlights_in_fur_color': None, 'activities': 'Eating, Foraging', 'interactions_with_humans': None}])

# rewriting squirrels_by_park to be more nicely formatted
squirrels_by_park = {
    'Union Square Park': [{'primary_fur_color': 'Gray', 'highlights_in_fur_color': None, 'activities': 'Eating, Foraging', 'interactions_with_humans': None},
                          {'primary_fur_color': 'Gray', 'highlights_in_fur_color': 'Cinnamon', 'activities': 'Climbing, Eating', 'interactions_with_humans': None},
                          {'primary_fur_color': 'Cinnamon', 'highlights_in_fur_color': None, 'activities': 'Foraging', 'interactions_with_humans': 'Indifferent'},
                          {'primary_fur_color': 'Gray', 'highlights_in_fur_color': None, 'activities': 'Running, Digging', 'interactions_with_humans': 'Runs From'},
                          {'primary_fur_color': 'Gray', 'highlights_in_fur_color': None, 'activities': 'Digging', 'interactions_with_humans': 'Indifferent'},
                          {'primary_fur_color': 'Gray', 'highlights_in_fur_color': 'Black', 'activities': 'Climbing', 'interactions_with_humans': None},
                          {'primary_fur_color': 'Gray', 'highlights_in_fur_color': None, 'activities': 'Eating, Foraging', 'interactions_with_humans': None}],
    'Madison Square Park': [{'primary_fur_color': 'Gray', 'highlights_in_fur_color': None, 'activities': 'Sitting', 'interactions_with_humans': 'Indifferent'},
                            {'primary_fur_color': 'Gray', 'highlights_in_fur_color': 'Cinnamon', 'activities': 'Foraging', 'interactions_with_humans': 'Indifferent'},
                            {'primary_fur_color': 'Gray', 'highlights_in_fur_color': None, 'activities': 'Climbing, Foraging', 'interactions_with_humans': 'Indifferent'}]
}

# Assign squirrels_madison as the value to the 'Madison Square Park' key
squirrels_by_park['Madison Square Park'] = squirrels_madison

# Update squirrels_by_park with the squirrels_union tuple
squirrels_by_park.update([squirrels_union])

# Loop over the park_name in the squirrels_by_park dictionary 
for park_name in squirrels_by_park:
    # Safely print a list of the primary_fur_color for each squirrel in park_name
    print(park_name, [squirrel.get('primary_fur_color', 'N/A') for squirrel in squirrels_by_park[park_name]])  

'''
O código acima demonsstra como manipular dicionários em Python, incluindo a criação, atualização e iteração sobre eles. Ele também mostra como acessar valores de dicionários aninhados e como lidar com casos onde uma chave pode não existir, utilizando o método `get` para evitar erros.
'''