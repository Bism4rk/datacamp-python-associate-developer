min_num_beds = 2
min_sq_foot = 750
max_rent = 1900

num_beds = int(input("Enter the number of bedrooms: "))
sq_foot = int(input("Enter the square footage: "))
rent = int(input("Enter the monthly rent: "))

'''
As variáveis num_beds, sq_foot e rent foram dadas pelo exercício, aqui estão como inputs para facilitar o teste do código.
'''

# Check the number of beds
if num_beds < min_num_beds:
  print("Insufficient bedrooms")

# Check square feet
elif sq_foot <= min_sq_foot:
  print("Too small")
  
# Check the rent
elif rent > max_rent:
  print("Too expensive")

# If all conditions met
else:
  print("This looks promising!")

'''
O código acima mostra como usar condicionais para verificar se um imóvel atende a certos critérios. Ele verifica o número de quartos, a metragem quadrada e o aluguel mensal. Se algum critério não for atendido, uma mensagem apropriada é exibida. Se todos os critérios forem atendidos, uma mensagem positiva é exibida.
'''