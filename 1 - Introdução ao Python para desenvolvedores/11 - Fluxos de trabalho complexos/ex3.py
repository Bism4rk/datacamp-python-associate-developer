genre_sales = {
    "Horror": 2500000,
    "Mystery": 1500000,
    "Thriller": 3500000,
    "Romance": 2000000,
    "Sci-Fi": 1800000
}

# Loop through the dictionary
for genre, sale in genre_sales.items():
  
  # Check if genre is Horror or Mystery
  if genre == "Horror" or genre == "Mystery":
    print(genre, sale)
  
  # Check if genre is Thriller and sale is at least 3 million
  elif genre == "Thriller" and sale >= 3000000:
    print(genre, sale)

'''
O código acima mostra como usar um loop for para iterar sobre um dicionário em Python. Ele verifica o gênero de livros e suas vendas, imprimindo informações específicas para gêneros de Horror ou Mistério, ou para Thriller com vendas de pelo menos 3 milhões. Isso demonstra como aplicar condicionais dentro de loops para filtrar e exibir dados de forma dinâmica.
'''