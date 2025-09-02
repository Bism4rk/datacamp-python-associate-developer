playlist = [1, 'Blinding Lights', 'The Weeknd', 2, 'One Dance', 'Drake', 3, 'Uptown Funk', 'Mark Ronson', 4, 'Closer', 'The Chainsmokers', 5, 'One Kiss', 'Calvin Harris', 6, 'Mr. Brightside', 'The Killers']

# Find the second song
print(playlist[4])

# Get the last song's artist
print(playlist[-1])

# Print all songs in the playlist
print(playlist[1::3])

'''
O código acima mostra como acessar elementos específicos de uma lista em Python. A lista `playlist` contém informações sobre músicas, onde cada música é representada por um número, título e artista. 
- Usando `playlist[4]`, obtemos a segunda música da lista, o quinto elemento, que é 'One Dance'.
- Usando `playlist[-1]`, acessamos o último elemento da lista, que é o artista da última música, 'The Killers'.
- Usando `playlist[1::3]`, imprimimos todos os títulos das músicas na lista, começando do segundo elemento e pulando a cada três elementos, resultando em uma lista de títulos de músicas.
'''