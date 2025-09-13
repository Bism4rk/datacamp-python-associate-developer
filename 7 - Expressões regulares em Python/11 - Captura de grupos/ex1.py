import re

sentiment_analysis = ['Just got ur newsletter, those fares really are unbelievable. Write to statravelAU@gmail.com or statravelpo@hotmail.com. They have amazing prices', 'I should have paid more attention when we covered photoshop in my webpage design class in undergrad. Contact me Hollywoodheat34@msn.net.', 'hey missed ya at the meeting. Read your email! msdrama098@hotmail.com']

# Write a regex that matches email
regex_email = r"([A-Za-z0-9]+)@\S+"

for tweet in sentiment_analysis:
    # Find all matches of regex in each tweet
    email_matched = re.findall(regex_email, tweet)

    # Complete the format method to print the results
    print("Lists of users found in this tweet: {}".format(email_matched))

'''
O código acima demonstra como usar expressões regulares em Python para capturar grupos específicos de texto, como nomes de usuários em endereços de e-mail. A regex `r"([A-Za-z0-9]+)@\S+"` é usada para identificar e extrair a parte do nome de usuário antes do símbolo "@" em cada endereço de e-mail encontrado nos tweets da lista `sentiment_analysis`. A função `re.findall()` retorna todas as correspondências encontradas, que são então impressas no console.
'''