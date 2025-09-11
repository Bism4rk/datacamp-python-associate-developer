# Import the re module
import re

sentiment_analysis = "@robot9! @robot4& I have a good feeling that the show isgoing to be amazing! @robot9$ @robot7%"

# Write the regex
regex = r"@robot\d\W"

# Find all matches of regex
print(re.findall(regex, sentiment_analysis))

'''
O código acima encontra todas as ocorrências do padrão definido pela expressão regular na string `sentiment_analysis`. A expressão `@robot\d\W` procura por substrings que começam com "@robot", seguidas por um dígito (`\d`) e um caractere que não seja uma letra, número ou sublinhado (`\W`). O resultado é uma lista de todas as correspondências encontradas.
'''