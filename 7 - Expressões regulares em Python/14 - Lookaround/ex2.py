import re

cellphones = ['4564-646464-01', '345-5785-544245', '6476-579052-01']

for phone in cellphones:
	# Get all phone numbers not preceded by area code
	number = re.findall(r"(?<![0-9]{3}-)[0-9]{4}-[0-9]{6}-[0-9]{2}", phone)
	print(number)

for phone in cellphones:
# Get all phone numbers not followed by optional extension
    number = re.findall(r"[0-9]{3}-[0-9]{4}-[0-9]{6}(?!-[0-9]{2})", phone)
    print(number)

'''
O código acima demonstra como usar lookbehind negativo e lookahead negativo em expressões regulares com Python. Ele procura por números de telefone que não são precedidos por um código de área (lookbehind negativo) e por números de telefone que não são seguidos por uma extensão opcional (lookahead negativo) na lista de celulares. Os números correspondentes são então impressos.
'''