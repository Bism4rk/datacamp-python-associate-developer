squirrels_by_park = {'Tompkins Square Park': [{'primary_fur_color': 'Gray', 'highlights_in_fur_color': 'Gray', 'activities': 'Foraging', 'interactions_with_humans': 'Approaches'}, {'primary_fur_color': 'Gray', 'highlights_in_fur_color': 'Gray', 'activities': 'Climbing (down tree)', 'interactions_with_humans': 'Indifferent'}, {'primary_fur_color': 'Gray', 'highlights_in_fur_color': 'Gray', 'interactions_with_humans': 'Indifferent'}, {'primary_fur_color': 'Gray', 'highlights_in_fur_color': 'Gray', 'activities': 'Foraging', 'interactions_with_humans': 'Indifferent'}], 'Union Square Park': [{'primary_fur_color': 'Gray', 'highlights_in_fur_color': None, 'activities': 'Eating, Foraging', 'interactions_with_humans': None}, {'primary_fur_color': 'Cinnamon', 'highlights_in_fur_color': None, 'activities': 'Foraging', 'interactions_with_humans': None}, {'primary_fur_color': 'Gray', 'highlights_in_fur_color': None, 'activities': 'Eating, Foraging', 'interactions_with_humans': None}, {'primary_fur_color': 'Gray', 'highlights_in_fur_color': None, 'activities': 'Digging', 'interactions_with_humans': 'Indifferent'}]}

# Use a for loop to iterate over the squirrels in Tompkins Square Park:
for squirrel in squirrels_by_park["Tompkins Square Park"]:
	# Safely print the activities of each squirrel or None
    print(squirrel.get("activities"))
    
# Print the list of 'Cinnamon' primary_fur_color squirrels in Union Square Park
print([squirrel for squirrel in squirrels_by_park["Union Square Park"] if "Cinnamon" in squirrel["primary_fur_color"]])

'''
O código acima demonstra como acessar e manipular um dicionário com dicionários aninhados em Python. O dicionário `squirrels_by_park` contém informações sobre esquilos em diferentes parques, incluindo cor do pelo, atividades e interações com humanos. O código itera sobre os esquilos no Tompkins Square Park, imprimindo suas atividades, e filtra os esquilos no Union Square Park para encontrar aqueles com cor de pelo 'Cinnamon'. A função `get` é usada para evitar erros caso uma chave não exista, retornando `None` quando necessário.
'''