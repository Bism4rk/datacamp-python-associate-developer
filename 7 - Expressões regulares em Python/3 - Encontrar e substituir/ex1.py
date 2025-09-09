movies = [
    "The actor actor was seen in the movie.",
    "The actor was seen in the movie.",
    "The actor actor actor was seen in the movie."
]

for movie in movies:
  	# If actor is not found between character 37 and 41 inclusive
    # Print word not found
    if movie.find("actor", 37, 42) == -1:
        print("Word not found")
    # Count occurrences and replace two with one
    elif movie.count("actor") == 2:  
        print(movie.replace("actor actor", "actor"))
    else:
        # Replace three occurrences with one
        print(movie.replace("actor actor actor", "actor"))

'''
O código acima demonstra como usar métodos de string em Python para encontrar, contar e substituir substrings dentro de uma lista de strings. Ele verifica se a palavra "actor" está presente em uma posição específica da string, conta quantas vezes a palavra aparece e substitui múltiplas ocorrências por uma única ocorrência. Dependendo do número de vezes que "actor" aparece, ele realiza a substituição apropriada ou indica que a palavra não foi encontrada na posição especificada.
'''