# Define a function called concat
def concat(*args):
  
  # Create an empty string
  result = ""
  
  # Iterate over the Python args tuple
  for arg in args:
    result += " " + arg
  return result

# Call the function
print(concat("Python", "is", "great!"))

'''
O código acima demonstra como usar argumentos arbitrários em uma função Python. A função `concat` aceita um número variável de argumentos e os concatena em uma única string, separando-os por espaços. A função é chamada com três strings, e o resultado é impresso.
'''