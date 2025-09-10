# Import Template
from string import Template

# Create a template
wikipedia = Template("$tool is a $description")

tool1 = "Natural Language Toolkit"
description1 = "Python library for natural language processing"

tool2 = "Pandas"
description2 = "Python library for data manipulation and analysis"

tool3 = "Matplotlib"
description3 = "Python library for data visualization"

# Substitute variables in template
print(wikipedia.substitute(tool=tool1, description=description1))
print(wikipedia.substitute(tool=tool2, description=description2))
print(wikipedia.substitute(tool=tool3, description=description3))

'''
O código acima demonstra como usar a classe Template do módulo string para criar e manipular templates de strings em Python. Ele define um template com dois placeholders ($tool e $description) e substitui esses placeholders por valores específicos usando o método substitute(). O resultado é uma série de strings formatadas que descrevem diferentes bibliotecas Python.
'''