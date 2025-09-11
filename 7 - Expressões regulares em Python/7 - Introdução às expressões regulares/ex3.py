import re

sentiment_analysis = "He#newHis%newTin love with$newPscrappy. #8break%He is&newYmissing him@newLalready"

# Write a regex to match pattern separating sentences
regex_sentence = r"\W\dbreak\W"

# Replace the regex_sentence with a space
sentiment_sub = re.sub(regex_sentence, " ", sentiment_analysis)

# Write a regex to match pattern separating words
regex_words = r"\Wnew\w"

# Replace the regex_words and print the result
sentiment_final = re.sub(regex_words, " ", sentiment_sub)
print(sentiment_final)

'''
O código acima demonstra como usar expressões regulares para separar frases e palavras em uma string. Primeiro, ele substitui a ocorrência de "break" por um espaço, efetivamente separando as frases. Em seguida, ele remove todas as ocorrências da palavra "new" que estão cercadas por caracteres não alfanuméricos, resultando em uma string mais limpa.
'''