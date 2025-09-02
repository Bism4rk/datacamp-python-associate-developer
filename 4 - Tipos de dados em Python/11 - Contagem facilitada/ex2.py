# Import the Counter object
from collections import Counter
from penguins import penguins

# Create a Counter of the penguins list: penguins_species_counts
penguins_species_counts = Counter([penguin['Species'] for penguin in penguins])

# Find the 3 most common species counts
print(penguins_species_counts.most_common(3))

'''
O código acima demonstra como usar o objeto Counter da biblioteca collections para contar a ocorrência de certos elementos em uma lista e como encontrar os mais comuns. Neste caso, ele conta quantos pinguins pertencem a cada espécie a partir de uma lista de dicionários que contém informações sobre cada pinguim. A saída será uma lista de tuplas, onde cada tupla contém uma espécie e o número de ocorrências dessa espécie na lista de pinguins, ordenada da mais comum para a menos comum.
'''