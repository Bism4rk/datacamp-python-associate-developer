import re

sentiment_analysis = "Was intending to finish editing my 536-page novel manuscript tonight, but that will probably not happen. And only 12 pages are left"

# Write a lazy regex expression 
numbers_found_lazy = re.findall(r"\d+?", sentiment_analysis)

# Print out the result
print(numbers_found_lazy)

# Write a greedy regex expression 
numbers_found_greedy = re.findall(r"\d+", sentiment_analysis)

# Print out the result
print(numbers_found_greedy)

'''
O código acima demonstra a diferença entre correspondência gananciosa e não gananciosa em expressões regulares usando Python. A função re.findall() é utilizada para encontrar todas as ocorrências de um padrão específico em uma string. A expressão regular com correspondência não gananciosa (lazy) retorna cada dígito individualmente, enquanto a expressão com correspondência gananciosa (greedy) retorna o número completo como uma única string.
'''