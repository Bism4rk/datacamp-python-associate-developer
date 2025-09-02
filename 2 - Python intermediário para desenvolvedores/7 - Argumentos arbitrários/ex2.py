# Define a function called concat
def concat(**kwargs):
  
  # Create an empty string
  result = ""
  
  # Iterate over the Python kwargs
  for kwarg in kwargs.values():
    result += " " + kwarg
  return result

# Call the function
print(concat(start="Python", middle="is", end="great!"))

'''
O código acima demonstra como usar argumentos arbitrários de palavra-chave em uma função Python. A função `concat` aceita um número variável de argumentos de palavra-chave e os concatena em uma única string, separando-os por espaços. A função é chamada com três argumentos de palavra-chave, e o resultado é impresso.
'''