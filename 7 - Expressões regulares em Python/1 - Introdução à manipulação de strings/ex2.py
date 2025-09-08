movie1 = "the most significant tension of _election_ is the potential relationship between a teacher and his student ."
movie2 = "the most significant tension of _rushmore_ is the potential relationship between a teacher and his student ."

# Select the first 32 characters of movie1
first_part = movie1[:32]

# Select from 43rd character to the end of movie1
last_part = movie1[42:]

# Select from 33rd to the 42nd character
middle_part = movie2[32:42]

# Print concatenation and movie2 variable
print(first_part +middle_part+last_part) 
print(movie2)

'''
O código acima demonstra como manipular strings em Python, especificamente como fatiar (slice) partes de uma string e concatená-las. Ele seleciona diferentes partes da variável `movie1` e `movie2`, combina essas partes e imprime o resultado, mostrando como é possível construir novas strings a partir de substrings existentes.
'''