def clean_string(text):
  
  # Add a single-line docstring
  """Swap spaces to underscores and convert text to lowercase"""
  
  no_spaces = text.replace(" ", "_")
  clean_text = no_spaces.lower()
  return clean_text

# Access the docstring
print(clean_string.__doc__)

'''
O código acima mostra como definir uma docstring de uma linha para uma função personalizada em Python. A função `clean_string` substitui os espaços por sublinhados e converte o texto para minúsculas. A docstring é acessada e impressa, demonstrando como documentar funções de forma concisa.
'''