# Create the clean_string function
def clean_string(text):
  
  # Replace spaces with underscores
  no_spaces = text.replace(" ", "_")
  
  # Convert to lowercase
  clean_text = no_spaces.lower()
  
  # Return the final text as an output
  return clean_text

converted_text = clean_string("I LoVe dATaCamP!")
print(converted_text)

'''
O código acima mostra como definir uma função personalizada em Python. Esta função, chamada `clean_string`, recebe um texto como entrada, substitui os espaços por sublinhados, converte todo o texto para minúsculas e retorna o resultado. A função é então chamada com a string "I LoVe dATaCamP!" e o resultado é impresso.
'''