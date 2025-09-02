mutants = ['charles xavier', 
            'bobby drake', 
            'kurt wagner', 
            'max eisenhardt', 
            'kitty pryde']


powers = ['telepathy', 
          'cryokinesis', 
          'teleportation', 
          'magnetism', 
          'phasing']

# Create a zip object from mutants and powers: z1
z1 = zip(mutants, powers)

# Print the tuples in z1 by unpacking with *
print(*z1)

# Re-create a zip object from mutants and powers: z1
z1 = zip(mutants, powers)

# 'Unzip' the tuples in z1 by unpacking with * and zip(): result1, result2
result1, result2 = zip(*z1)

# Check if unpacked tuples are equivalent to original tuples
print(result1 == mutants)
print(result2 == powers)

'''
O código acima demonstra como usar a função `zip()` para combinar duas listas em um iterador de tuplas. Primeiro, duas listas são criadas: `mutants` e `powers`. A função `zip()` é usada para criar um iterador que agrupa os elementos correspondentes das duas listas em tuplas. As tuplas resultantes são impressas usando o operador de desempacotamento `*`. Em seguida, o iterador é recriado e as tuplas são "desempacotadas" novamente usando `zip(*z1)`, permitindo verificar se os resultados correspondem às listas originais. Isso mostra como a função `zip()` pode ser útil para agrupar dados relacionados de diferentes coleções.
'''