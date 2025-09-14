import re

html_tags = ['<body>Welcome to our course! It would be an awesome experience</body>', '<article>To be a data scientist, you need to have knowledge in statistics and mathematics</article>', '<nav>About me Links Contact me!']

for string in html_tags:
    # Complete the regex and find if it matches a closed HTML tags
    match_tag =  re.match(r"<(\w+)>.*?</\1>", string)
 
    if match_tag:
        # If it matches print the first group capture
        print("Your tag {} is closed".format(match_tag.group(1))) 
    else:
        # If it doesn't match capture only the tag 
        notmatch_tag = re.match(r"<(\w+)>", string)
        # Print the first group capture
        print("Close your {} tag!".format(notmatch_tag.group(1)))

'''
O código acima demonstra como usar referências inversas em expressões regulares para verificar se as tags HTML estão corretamente fechadas. A regex r"<(\w+)>.*?</\1>" captura uma tag de abertura e verifica se há uma tag de fechamento correspondente. Se a tag estiver fechada corretamente, o nome da tag é impresso; caso contrário, uma mensagem solicitando o fechamento da tag é exibida.
'''