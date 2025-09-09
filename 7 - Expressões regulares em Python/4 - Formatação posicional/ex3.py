# Import datetime 
from datetime import datetime

# Assign date to get_date
get_date = datetime.now()

# Add named placeholders with format specifiers
message = "Good morning. Today is {today:%B %d, %Y}. It's {today:%H:%M} ... time to work!"

# Use the format method replacing the placeholder with get_date
print(message.format(today=get_date))

'''
O código acima demonstra como usar formatação posicional com expressões regulares em Python. Ele importa o módulo datetime para obter a data e hora atuais, cria uma mensagem com espaços reservados nomeados que incluem especificadores de formato para exibir a data e hora em um formato legível, e finalmente imprime a mensagem formatada substituindo o espaço reservado pelo valor atual da data e hora.
'''