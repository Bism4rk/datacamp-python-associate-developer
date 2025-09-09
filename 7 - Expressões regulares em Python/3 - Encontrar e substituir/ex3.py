movies ="the rest of the story is important because all it does isn't serve as a mere backdrop for the two stars to share the screen ."

# Replace negations 
movies_no_negation = movies.replace("isn't", "is")

# Replace important
movies_antonym = movies_no_negation.replace("important", "insignificant")

# Print out
print(movies_antonym)

'''
O código acima demonstra como usar o método `replace()` em Python para substituir substrings dentro de uma string. Primeiro, ele substitui a palavra "isn't" por "is", removendo a negação. Em seguida, substitui a palavra "important" por seu antônimo "insignificant". Finalmente, imprime a string modificada. Isso ilustra como manipular strings para alterar seu significado ou contexto.
'''