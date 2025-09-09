movies = [
    "Show me the money!",
    "Money Never Sleeps",
    "For Love or Money",
    "No Country for Old Men",
    "The Color of Money",
    "Blood Money",
    "Funny Money",
    "Honey, I Shrunk the Kids",
    "A Fistful of Dollars",
    "Wall Street: Money Talks"
]

for movie in movies:
  # Find the first occurrence of word
    print(movie.find("money"))

for movie in movies:
    try:
    # Find the first occurrence of word
        print(movie.index("money"))
    except ValueError:
        print("substring not found")

'''
O código acima demonstra como usar os métodos de string `find()` e `index()` em Python para localizar a posição da primeira ocorrência de uma substring dentro de uma lista de strings. O método `find()` retorna -1 se a substring não for encontrada, enquanto o método `index()` lança uma exceção `ValueError` nesse caso. O código inclui um bloco `try-except` para lidar com essa exceção ao usar o método `index()`, garantindo que o programa continue a funcionar mesmo quando a substring não está presente.
'''