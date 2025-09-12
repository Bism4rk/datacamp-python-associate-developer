import re

# Write a regex to match a valid email address
regex = r"[A-Za-z0-9!#%&*\$\.]+@\w+\.com"

emails = ['n.john.smith@gmail.com', '87victory@hotmail.com', '!#mary-=@msca.net']


for example in emails:
	# Match the regex to the string
	if re.match(regex, example):
		# Complete the format method to print out the result
		print("The email {email_example} is a valid email".format(email_example=example))
	else:
		print("The email {email_example} is invalid".format(email_example=example))   

'''
O código acima demonstra como usar caracteres especiais em expressões regulares para validar endereços de email. A regex definida procura por padrões comuns em endereços de email, como letras, números e certos caracteres especiais antes do símbolo "@" e um domínio que termina com ".com". O código então verifica cada email na lista e imprime se é válido ou inválido com base na correspondência da regex.
'''