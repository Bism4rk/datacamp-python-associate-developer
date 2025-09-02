# Define clean_text
def clean_text(text, lower=True):
  if lower == False:
    clean_text = text.replace(" ", "_")
    return clean_text
  else:
    clean_text = text.replace(" ", "_")
    clean_text = clean_text.lower()
    return clean_text
  
# Define clean_text
def clean_text(text, remove=None):
  if remove != None:
    clean_text = text.replace(remove, "")
    clean_text = clean_text.lower()
    return clean_text
  else:
    clean_text = text.lower()
    return clean_text
  
'''
O código acima demonstra dois tipos de parâmetros que podem ser usados em uma função personalizada em Python: parâmetros padrão e de palavra-chave. A função `clean_text` aceita um texto e um parâmetro opcional `remove`. Se `remove` for fornecido, ele remove esse caractere do texto antes de convertê-lo para minúsculas. Caso contrário, apenas converte o texto para minúsculas. Isso ilustra como os parâmetros padrão e de palavra-chave podem ser utilizados para tornar as funções mais flexíveis.
'''