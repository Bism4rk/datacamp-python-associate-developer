import re

# Write a regex that matches sentences with the optional words
regex_positive = r"(love|like|enjoy).+?(movie|concert)\s(.+?)\."

sentiment_analysis = ['I totally love the concert The Book of Souls World Tour. It kinda amazing!', 'I enjoy the movie Wreck-It Ralph. I watched with my boyfriend.', "I still like the movie Wish Upon a Star. Too bad Disney doesn't show it anymore."]


for tweet in sentiment_analysis:
	# Find all matches of regex in tweet
    positive_matches = re.findall(regex_positive, tweet)
    
    # Complete format to print out the results
    print("Positive comments found {}".format(positive_matches))

'''
O código acima demonstra como usar expressões regulares em Python para analisar sentimentos em textos. Ele define uma expressão regular que procura por frases que contenham palavras positivas como "love", "like" ou "enjoy", seguidas por "movie" ou "concert" e o nome do filme ou concerto. Em seguida, ele percorre uma lista de análises de sentimentos, encontra todas as correspondências da expressão regular em cada tweet e imprime os comentários positivos encontrados.
'''