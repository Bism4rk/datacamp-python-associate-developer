squirrels = [('Marcus Garvey Park', ('Black', 'Cinnamon', 'Cleaning', None)), ('Highbridge Park', ('Gray', 'Cinnamon', 'Running, Eating', 'Runs From, watches us in short tree')), ('Madison Square Park', ('Gray', None, 'Foraging', 'Indifferent')), ('City Hall Park', ('Gray', 'Cinnamon', 'Eating', 'Approaches')), ('J. Hood Wright Park', ('Gray', 'White', 'Running', 'Indifferent')), ('Seward Park', ('Gray', 'Cinnamon', 'Eating', 'Indifferent')), ('Union Square Park', ('Gray', 'Black', 'Climbing', None)), ('Tompkins Square Park', ('Gray', 'Gray', 'Lounging', 'Approaches'))]

# Create an empty dictionary: squirrels_by_park
squirrels_by_park = {}

# Loop over the squirrels list and unpack each tuple
for park, squirrel_details in squirrels:
    # Add each squirrel_details to the squirrels_by_park dictionary 
    squirrels_by_park[park] = squirrel_details
    
# Sort the squirrels_by_park dict alphabetically by park
for park in sorted(squirrels_by_park):
    # Print each park and its value in squirrels_by_park
    print(f'{park}: {squirrels_by_park[park]}')

'''
O código acima demonstra como criar um dicionário a partir de uma lista de tuplas, onde cada tupla contém o nome de um parque e detalhes sobre esquilos. A lista `squirrels` contém informações sobre esquilos em diferentes parques, incluindo cor, comportamento e interações. O loop `for` percorre cada tupla, desempacotando o nome do parque e os detalhes do esquilo, e adiciona essas informações ao dicionário `squirrels_by_park`. Em seguida, o dicionário é ordenado alfabeticamente pelos nomes dos parques e impresso, mostrando como organizar e acessar dados de forma eficiente.
'''