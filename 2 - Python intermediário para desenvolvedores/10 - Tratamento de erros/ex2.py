def snake_case(text):
  # Check the data type
  if type(text) == str:
    clean_text = text.replace(" ", "_")
    clean_text = clean_text.lower()
  else:
    # Return a TypeError error if the wrong data type was used
    raise TypeError("The snake_case() function expects a string as an argument, please check the data type provided.")
    
snake_case("User Name 187")

'''
O código acima demonstra como usar 'raise' para lançar um erro de tipo personalizado quando a função `snake_case` recebe um argumento que não é uma string. A função tenta substituir espaços por underscores e converter o texto para minúsculas, mas se o argumento não for do tipo string, um `TypeError` é levantado com uma mensagem explicativa. Isso ajuda a garantir que a função seja usada corretamente e facilita a depuração de erros.
'''