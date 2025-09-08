file = "mtv films election, a high school comedy, is a current example\nfrom there, director steven spielberg wastes no time, taking us into the water on a midnight swim"

# Split string at line boundaries
file_split = file.splitlines()

# Print file_split
print(file_split)

# Complete for-loop to split by commas
for substring in file_split:
    substring_split = substring.split(sep=",")
    print(substring_split)

'''
O código acima demonstra como manipular strings em Python, especificamente como dividir uma string em várias linhas e, em seguida, dividir cada linha em substrings usando uma vírgula como delimitador. A função `splitlines()` é usada para separar a string original em uma lista de linhas, e um loop `for` itera sobre cada linha para dividi-la ainda mais em substrings. Cada etapa é impressa para mostrar o resultado das operações de manipulação de strings.
'''