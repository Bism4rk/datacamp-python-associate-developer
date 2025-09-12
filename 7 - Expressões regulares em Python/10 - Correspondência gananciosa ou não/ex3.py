import re

sentiment_analysis = "Put vacation photos online (They were so cute) a few yrs ago. PC crashed, and now I forget the name of the site (I'm crying)."

# Write a lazy regex expression
sentences_found_lazy = re.findall(r"\(.*?\)", sentiment_analysis)

# Print out the results
print(sentences_found_lazy)

# Write a greedy regex expression 
numbers_found_greedy = re.findall(r"\d+", sentiment_analysis)

# Print out the result
print(numbers_found_greedy)

'''
O código acima demonstra a diferença entre correspondência gananciosa e não gananciosa em expressões regulares usando Python. A função re.findall() é utilizada para encontrar todas as ocorrências de um padrão específico em uma string. A expressão regular com correspondência não gananciosa (lazy) retorna o texto dentro dos parênteses, enquanto a expressão com correspondência gananciosa (greedy) retorna os números completos como uma única string.
'''