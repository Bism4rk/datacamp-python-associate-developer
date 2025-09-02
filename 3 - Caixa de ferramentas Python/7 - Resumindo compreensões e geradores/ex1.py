import pandas as pd

df = pd.read_csv('tweets.csv')

# Extract the created_at column from df: tweet_time
tweet_time = df['created_at']

# Extract the clock time: tweet_clock_time
tweet_clock_time = [entry[11:19] for entry in tweet_time]

# Print the extracted times
print(tweet_clock_time)

'''
O código acima demonstra como extrair a parte do tempo de uma coluna de data e hora em um DataFrame do Pandas usando uma compreensão de lista. Ele extrai os horários dos tweets no formato 'HH:MM:SS' a partir da coluna 'created_at'. A saída será uma lista de strings representando os horários dos tweets.
'''
