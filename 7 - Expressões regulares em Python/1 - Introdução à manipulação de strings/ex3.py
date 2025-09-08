movie = "oh my God! desserts I stressed was an ugly movie"

# Get the word
movie_title = movie[11:30]

# Obtain the palindrome
palindrome = movie_title[::-1]

# Print the word if it's a palindrome
if movie_title == palindrome:
	print(movie_title)
	
'''
O código acima demonstra como manipular strings em Python, especificamente como fatiar (slice) uma parte de uma string e verificar se essa parte é um palíndromo (uma palavra ou frase que lê da mesma forma de trás para frente). Ele extrai uma substring da variável `movie`, inverte essa substring e compara as duas versões para determinar se são iguais, imprimindo a substring se for um palíndromo.
'''