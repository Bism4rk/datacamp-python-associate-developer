float1 = 0.000010
float2 = 0.0000100
float3 = 0.0000001

# Print floats 1, 2, and 3
print(float1)
print(float2)
print(float3)

# Print floats 2 and 3 using the f string formatter
print(f"{float2:f}")
print(f"{float3:f}")

# Print float 3 with a 7 f string precision
print(f"{float3:.7f}")

'''
O código acima demonstra a representação de números de ponto flutuante em Python. Os números são representados com precisão de 6 casas decimais por padrão, mas podem ser formatados para exibir mais casas decimais usando o formato f-string. A precisão pode ser ajustada conforme necessário, como mostrado no exemplo com float3.
'''