# Create the convert_data_type function
def convert_data_structure(data, data_type="list"):
  # Add a multi-line docstring
  """
  Convert a data structure to a list, tuple, or set.
  
  Args:
  	data (list, tuple, or set): A data structure to be converted.
    data_type (str): String representing the type of structure to convert data to.
    
  Returns:
  	data (list, tuple, or set): Converted data structure
  """
  if data_type == "tuple":
    data = tuple(data)
  elif data_type == "set":
    data = set(data)
  else:
    data = list(data)
  return data

print(help(convert_data_structure))

'''
O código acima demonstra como definir uma docstring multi-linha para uma função personalizada em Python. A função `convert_data_structure` aceita um conjunto de dados e um tipo de dado opcional (`data_type`). Dependendo do valor de `data_type`, ela converte os dados para uma tupla, conjunto ou lista. A docstring fornece informações sobre os argumentos e o retorno da função, e é acessada usando a função `help()`.
'''