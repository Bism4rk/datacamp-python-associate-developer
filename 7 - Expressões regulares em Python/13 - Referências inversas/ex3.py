import re

sentiment_analysis = "['@marykatherine_q i know! I heard it this morning and wondered the same thing. Moscooooooow is so behind the times', 'Staying at a friends house...neighborrrrrrrs are so loud-having a party', 'Just woke up an already have read some e-mail']"


# Complete the regex to match an elongated word
regex_elongated = r"\w*(\w)\1\w*"

for tweet in sentiment_analysis:
	# Find if there is a match in each tweet 
	match_elongated = re.search(regex_elongated, tweet)
    
	if match_elongated:
		# Assign the captured group zero 
		elongated_word = match_elongated.group(0)
        
		# Complete the format method to print the word
		print("Elongated word found: {word}".format(word=elongated_word))
	else:
		print("No elongated word found") 
		
'''
O código acima demonstra como usar expressões regulares em Python para identificar palavras alongadas (com letras repetidas) em uma análise de sentimento. A regex `r"\w*(\w)\1\w*"` é usada para capturar qualquer palavra que contenha uma letra repetida consecutivamente. O código percorre cada tweet na variável `sentiment_analysis`, procurando por correspondências e imprimindo as palavras alongadas encontradas ou indicando que nenhuma foi encontrada.
'''