import re

# Write a regex to check if the password is valid
regex = r"[a-zA-Z0-9*#\$%!&\.]{8,20}"

passwords = ['Apple34!rose', 'My87hou#4$', 'abc123']

for example in passwords:
  	# Scan the strings to find a match
    if re.match(regex, example):
    # Complete the format method to print out the result
        print("The password {pass_example} is a valid password".format(pass_example=example))
    else:
        print("The password {pass_example} is invalid".format(pass_example=example))   

'''
O código acima demonstra como usar expressões regulares em Python para validar senhas com critérios específicos. A regex definida procura por senhas que contenham entre 8 e 20 caracteres, incluindo letras maiúsculas e minúsculas, números e certos caracteres especiais. O código então verifica cada senha na lista e imprime se é válida ou inválida com base na correspondência da regex.
'''