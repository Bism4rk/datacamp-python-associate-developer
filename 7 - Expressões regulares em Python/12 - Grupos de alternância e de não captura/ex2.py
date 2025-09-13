import re

# Write a regex that matches sentences with the optional words
regex_negative = r"(hate|dislike|disapprove).+?(?:movie|concert)\s(.+?)\."


sentiment_analysis = ['That was horrible! I really dislike the movie The cabin and the ant. So boring.', "I disapprove the movie Honest with you. It's full of cliches.", 'I dislike very much the concert After twelve Tour. The sound was horrible.']


for tweet in sentiment_analysis:
	# Find all matches of regex in tweet
    negative_matches = re.findall(regex_negative, tweet)
    
    # Complete format to print out the results
    print("Negative comments found {}".format(negative_matches))

'''
O código acima demonstra como usar expressões regulares em Python para analisar sentimentos negativos em textos. Ele define uma expressão regular que procura por frases que contenham palavras negativas como "hate", "dislike" ou "disapprove", seguidas por "movie" ou "concert" e o nome do filme ou concerto. Em seguida, ele percorre uma lista de análises de sentimentos, encontra todas as correspondências da expressão regular em cada tweet e imprime os comentários negativos encontrados.
'''