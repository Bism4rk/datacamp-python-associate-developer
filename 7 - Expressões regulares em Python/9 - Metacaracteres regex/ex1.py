import re

sentiment_analysis = [
    "aa_file.txt some text",
    "ae_file.txt some text",
    "ai_file.txt some text",
    "ao_file.txt some text",
    "au_file.txt some text",
    "ea_file.txt some text",
    "ee_file.txt some text"
	]

# Write a regex to match text file name
regex = r"^[aeiouAEIOU]{2,3}.+txt"

for text in sentiment_analysis:
	# Find all matches of the regex
	print(re.findall(regex, text))
    
	# Replace all matches with empty string
	print(re.sub(regex, "", text))
	
'''
O código acima demonstra como usar expressões regulares em Python para encontrar e substituir padrões em uma lista de strings. A regex definida procura por nomes de arquivos que começam com duas ou três vogais (maiúsculas ou minúsculas) seguidas por qualquer caractere e terminam com ".txt". O código então imprime os resultados das correspondências encontradas e as strings resultantes após a substituição dos padrões encontrados por uma string vazia.
'''