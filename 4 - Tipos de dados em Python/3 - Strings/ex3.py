girl_names = ['Jada', 'Emily', 'Ava', 'Serenity', 'Claire', 'Sophia', 'Sarah', 'Ashley', 'Chaya', 'Abigail', 'Zoe', 'Leah', 'Hailey', 'Ava', 'Olivia', 'Emma', 'Chloe', 'Sophia', 'Aaliyah', 'Angela', 'Camila', 'Savannah', 'Serenity', 'Fatoumata']

# Store a list of girl_names that start with s: names_with_s
names_with_s = [name for name in girl_names if name.lower().startswith('s')]

print(names_with_s)

# Store a list of girl_names that contain angel: names_with_angel
names_with_angel = [name for name in girl_names if 'angel' in name.lower()]

print(names_with_angel)

'''
O código acima demonstra como usar métodos de compreensão de listas para filtrar nomes de meninas com base em critérios específicos e como usar métodos de string para verificar condições. A lista `girl_names` contém uma variedade de nomes femininos. A primeira compreensão de lista cria `names_with_s`, que inclui apenas os nomes que começam com a letra 's', enquanto a segunda cria `names_with_angel`, que inclui nomes que contêm a substring 'angel'. Ambas as listas são impressas, mostrando como é possível extrair informações específicas de uma lista maior de forma eficiente.
'''