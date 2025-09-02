top_ten_girl_names = [(1, 'Jada'), (2, 'Emily'), (3, 'Ava'), (4, 'Serenity'), (5, 'Claire'), (6, 'Sophia'), (7, 'Sarah'), (8, 'Ashley'), (9, 'Chaya'), (10, 'Abigail')]

# Loop over top_ten_girl_names and unpack each tuple into top_ten_rank and name
for top_ten_rank, name in top_ten_girl_names:
  	# Print each name in the proper format
    print(f"Rank #: {top_ten_rank} - {name}")

'''
O código acima demonstra como iterar sobre uma lista de tuplas, onde cada tupla contém um ranking e um nome, e como usar strings formatados para exibir os resultados de forma clara. A lista '`top_ten_girl_names`' contém os dez nomes mais populares de meninas, cada um associado a um ranking. O loop `for` percorre cada tupla, desempacotando o ranking e o nome, e imprime uma mensagem formatada que inclui ambos. Isso é útil para exibir dados de forma organizada e legível.
'''