# Import the Counter object
from collections import Counter
from penguins import penguins

# Create a Counter of the penguins sex using a list comp
penguins_sex_counts = Counter([penguin['Sex'] for penguin in penguins])

# Print the penguins_sex_counts
print(penguins_sex_counts)

'''
O código acima demonstra como usar o objeto Counter da biblioteca collections para contar a ocorrência de certos elementos em uma lista. Neste caso, ele conta quantos pinguins são do sexo masculino e feminino a partir de uma lista de dicionários que contém informações sobre cada pinguim. A saída será um dicionário com as chaves sendo os sexos ('MALE' e 'FEMALE') e os valores sendo o número de ocorrências de cada sexo na lista de pinguins.
'''