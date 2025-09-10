# Import template
from string import Template

tools = ['Natural Language Toolkit', '20', 'month']

# Select variables
our_tool = tools[0]
our_fee = tools[1]
our_pay = tools[2]

# Create template
course = Template("We are offering a 3-month beginner course on $tool just for $$ $fee ${pay}ly")

# Substitute identifiers with three variables
print(course.substitute(tool=our_tool, fee=our_fee, pay=our_pay))

'''
O código acima demonstra como usar a classe Template do módulo string para criar e manipular templates de strings em Python. Ele define um template com três placeholders ($tool, $fee e ${pay}) e substitui esses placeholders por valores específicos usando o método substitute(). O resultado é uma string formatada que descreve um curso oferecido, incluindo o nome da ferramenta, a taxa e a frequência de pagamento.
'''