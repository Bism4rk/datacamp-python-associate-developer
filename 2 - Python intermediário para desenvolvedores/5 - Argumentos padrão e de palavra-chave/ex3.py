# Create the convert_data_structure function
def convert_data_structure(data, data_type="list"):
  
  # If data_type is "tuple"
  if data_type == "tuple":
    data = tuple(data)
  
  # Else if data_type is set, convert to a set
  elif data_type == "set":
    data = set(data)
  else:
    data = list(data)
  return data

# Call the function to convert to a set
convert_data_structure({"a", 1, "b", 2, "c", 3}, data_type="set")

'''
O código acima demonstra como definir uma função personalizada em Python que usa argumentos padrão e de palavra-chave. A função `convert_data_structure` aceita um conjunto de dados e um tipo de dado opcional (`data_type`). Dependendo do valor de `data_type`, ela converte os dados para uma tupla, conjunto ou lista. Isso ilustra como os argumentos padrão e de palavra-chave podem ser usados para tornar as funções mais flexíveis.
'''