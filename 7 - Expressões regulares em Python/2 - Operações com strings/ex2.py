movie = "the film,however,is all good<\i>" 

# Remove tags happening at the end and print results
movie_tag = movie.rstrip("<\i>")
print(movie_tag)

# Split the string using commas and print results
movie_no_comma = movie_tag.split(",")
print(movie_no_comma)

# Join back together and print results
movie_join = " ".join(movie_no_comma)
print(movie_join)

'''
O código acima demonstra como manipular strings em Python. Ele remove uma tag específica do final de uma string, divide a string em uma lista de substrings usando uma vírgula como delimitador e, em seguida, junta essas substrings de volta em uma única string, separando-as por espaços. Cada etapa é impressa para mostrar o resultado das operações de manipulação de strings.
'''