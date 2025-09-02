boy_names = ['Josiah', 'Ethan', 'David', 'Jayden', 'Mason', 'Ryan', 'Christian', 'Isaiah', 'Jayden', 'Michael']
# The top ten boy names are:  as preamble
preamble = "The top ten boy names are: "

# , and as conjunction
conjunction = ", and"

# Combines the first 9 names in boy_names with a comma and space as first_nine_names
first_nine_names = ", ".join(boy_names[0:9])

# Print f-string preamble, first_nine_names, conjunction, the final item in boy_names and a period
print(f"{preamble}{first_nine_names}{conjunction} {boy_names[-1]}.")

'''
O código acima demonstra como usar o método .join() e strings formatadas (f-strings) para criar uma frase que lista os dez nomes mais populares de meninos. A variável `preamble` contém a introdução da frase, enquanto `conjunction` é usada para conectar o penúltimo e o último nome na lista. O método .join() combina os primeiros nove nomes com uma vírgula e um espaço, resultando em uma string formatada que é impressa de forma clara e concisa. Isso é útil para apresentar listas de forma legível e organizada.
'''