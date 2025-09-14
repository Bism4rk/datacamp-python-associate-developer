import re

sentiment_analysis = "You need excellent python skills to be a data scientist. Must be! Excellent python"

# Positive lookahead
look_ahead = re.findall(r"\w+(?=\spython)", sentiment_analysis)

# Print out
print(look_ahead)

# Positive lookbehind
look_behind = re.findall(r"(?<=[Pp]ython\s)\w+", sentiment_analysis)

# Print out
print(look_behind)

'''
O código acima demonstra como usar lookahead e lookbehind em expressões regulares com Python. Ele procura por palavras que são seguidas por "python" (lookahead) e por palavras que precedem "python" (lookbehind) na string de análise de sentimento. As palavras correspondentes são então impressas.
'''