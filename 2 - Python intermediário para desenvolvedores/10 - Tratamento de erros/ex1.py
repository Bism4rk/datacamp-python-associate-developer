def snake_case(text):
  # Attempt to clean the text
  try:
    # Swap spaces for underscores
    clean_text = text.replace(" ", "_")
    clean_text = clean_text.lower()
  # Run this code if an error occurs
  except:
    print("The snake_case() function expects a string as an argument, please check the data type provided.")
    
snake_case("User Name 187")

'''
O código acima demonstra como usar um bloco `try` e `except` para tratar erros ao tentar converter uma string em snake_case. A função `snake_case` tenta substituir espaços por underscores e converter o texto para minúsculas. Se ocorrer um erro, como passar um tipo de dado diferente de string, o bloco `except` captura o erro e imprime uma mensagem informando que a função espera uma string como argumento.
'''