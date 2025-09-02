release_date = 26
current_date = 22

# Create a conditional loop while current_date is less than or equal to the release_date
while current_date <= release_date:
  
  # Promote purchases
  if current_date <= 24:
    print("Purchase before the 25th for early access")
  
  # Check if the date is equal to the 25th
  elif current_date == 25:
    print("Coming soon")
  else:
    print("Available now!")
  
  # Increment current_date by one
  current_date += 1

'''
O código acima mostra como usar um loop while em Python. Ele verifica a data atual em relação à data de lançamento e imprime mensagens promocionais dependendo da data. Se a data atual for menor ou igual a 24, uma mensagem de compra antecipada é exibida. Se for 25, uma mensagem de "em breve" é mostrada. Caso contrário, indica que o produto já está disponível. O loop continua até que a data atual ultrapasse a data de lançamento.
'''