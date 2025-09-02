password = "not_very_secure_2023"

# Define the password_checker function
def password_checker(submission):
  
  # Check that the password variable and the submission match
  if password == submission:
    print("Successful login!")
  
  # Otherwise, print "Incorrect password"
  else:
    print("Incorrect password")

# Call the function    
password_checker("NOT_VERY_SECURE_2023")

'''
O código acima demonstra novamente como definir uma função personalizada em Python. A função `password_checker` recebe uma entrada chamada `submission` e verifica se ela corresponde à variável `password`. Se a senha estiver correta, imprime "Successful login!", caso contrário, imprime "Incorrect password". A função é chamada com uma senha incorreta para demonstrar o funcionamento.
'''