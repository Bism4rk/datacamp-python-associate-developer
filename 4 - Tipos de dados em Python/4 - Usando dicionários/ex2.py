from ex1 import squirrels_by_park

# Safely print 'Union Square Park' from the squirrels_by_park dictionary
print(squirrels_by_park.get('Union Square Park'))

# Safely print the type of 'Fort Tryon Park' from the squirrels_by_park dictionary
print(type(squirrels_by_park.get('Fort Tryon Park')))

# Safely print 'Central Park' from the squirrels_by_park dictionary or 'Not Found'
print(squirrels_by_park.get('Central Park', 'Not Found'))

'''
O código acima demonstra como acessar valores em um dicionário de forma segura usando o método `.get()`. A variável `squirrels_by_park` contém informações sobre esquilos em diferentes parques. O primeiro `print` exibe os detalhes do parque 'Union Square Park'. O segundo `print` mostra o tipo de valor associado ao parque 'Fort Tryon Park', que não existe no dicionário, resultando em `None`. O terceiro `print` tenta acessar 'Central Park', que também não está presente, e retorna 'Not Found' como valor padrão. Isso é útil para evitar erros ao acessar chaves inexistentes em um dicionário.
'''