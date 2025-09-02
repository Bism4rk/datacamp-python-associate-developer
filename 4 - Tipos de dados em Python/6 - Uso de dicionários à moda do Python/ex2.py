squirrels_by_park = {'Tompkins Square Park': [{'primary_fur_color': 'Gray', 'highlights_in_fur_color': 'Gray', 'activities': 'Foraging', 'interactions_with_humans': 'Approaches'}, {'primary_fur_color': 'Gray', 'highlights_in_fur_color': 'Gray', 'activities': 'Climbing (down tree)', 'interactions_with_humans': 'Indifferent'}, {'primary_fur_color': 'Gray', 'highlights_in_fur_color': 'Gray', 'activities': 'Foraging', 'interactions_with_humans': 'Indifferent'}, {'primary_fur_color': 'Gray', 'highlights_in_fur_color': 'Gray', 'activities': 'Foraging', 'interactions_with_humans': 'Indifferent'}], 'Union Square Park': [{'primary_fur_color': 'Gray', 'highlights_in_fur_color': None, 'activities': 'Eating, Foraging', 'interactions_with_humans': None}, {'primary_fur_color': 'Cinnamon', 'highlights_in_fur_color': None, 'activities': 'Foraging', 'interactions_with_humans': None}, {'primary_fur_color': 'Gray', 'highlights_in_fur_color': None, 'activities': 'Eating, Foraging', 'interactions_with_humans': None}, {'primary_fur_color': 'Gray', 'highlights_in_fur_color': None, 'activities': 'Digging', 'interactions_with_humans': 'Indifferent'}]}


# Check to see if Tompkins Square Park is in squirrels_by_park
if "Tompkins Square Park" in squirrels_by_park:
    # Print 'Found Tompkins Square Park'
    print('Found Tompkins Square Park')
    
# Check to see if Central Park is in squirrels_by_park
if "Central Park" in squirrels_by_park:
    # Print 'Found Central Park' if found
    print('Found Central Park')
else:
    # Print 'Central Park missing' if not found
    print('Central Park missing')

'''
O código acima demonstra como verificar a presença de chaves em um dicionário em Python. O primeiro `if` verifica se "Tompkins Square Park" está presente no dicionário `squirrels_by_park`, e se estiver, imprime uma mensagem confirmando sua presença. O segundo `if` verifica se "Central Park" está presente; se não estiver, imprime uma mensagem indicando que "Central Park" está ausente.
'''