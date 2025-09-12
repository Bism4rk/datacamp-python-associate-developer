# Import re
import re

string = "I want to see that <strong>amazing show</strong> again!"

# Write a regex to eliminate tags
string_notags = re.sub(r"<.+?>", "", string)

# Print out the result
print(string_notags)

'''
O código acima demonstra como usar expressões regulares com correspondência não gananciosa em Python. A função re.sub() é utilizada para substituir todas as ocorrências de um padrão específico em uma string por uma nova substring. Ele remove as tags HTML da string original, resultando em uma saída limpa sem as tags.
'''