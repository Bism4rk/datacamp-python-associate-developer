# Create an iterator for range(3): small_value
small_value = iter(range(3))

# Print the values in small_value
print(next(small_value))
print(next(small_value))
print(next(small_value))

# Loop over range(3) and print the values
for num in range(3):
    print(num)


# Create an iterator for range(10 ** 100): googol
googol = iter(range(10 ** 100))

# Print the first 5 values from googol
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))

'''
O código acima demonstra como criar e usar iteradores em Python. Primeiro, um iterador é criado para o intervalo de 0 a 2 usando `iter(range(3))`, e os valores são impressos usando `next()`. Em seguida, um loop `for` percorre o mesmo intervalo e imprime os valores. Depois, um iterador é criado para um intervalo muito grande (de 0 a 10 elevado a 100) e os primeiros cinco valores são impressos. Isso ilustra como os iteradores permitem trabalhar com sequências de números, mesmo que sejam muito grandes.
'''