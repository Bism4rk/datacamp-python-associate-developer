movie = "$I supposed that coming from MTV Films I should expect no less$"

# Convert to lowercase and print the result
movie_lower = movie.lower()
print(movie_lower)

# Remove specified character and print the result
movie_no_sign = movie_lower.strip("$")
print(movie_no_sign)

# Split the string into substrings and print the result
movie_split = movie_no_sign.split()
print(movie_split)

# Select root word and print the result
word_root = movie_split[1][:-2]
print(word_root)

'''
O código acima demonstra como manipular strings em Python. Ele converte uma string para minúsculas, remove caracteres específicos do início e do fim, divide a string em uma lista de palavras e extrai a raiz de uma palavra específica. Cada etapa é impressa para mostrar o resultado das operações de manipulação de strings.
'''