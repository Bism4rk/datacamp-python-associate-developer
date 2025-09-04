from ex1 import onebike_durations

# Calculate shortest and longest trips
shortest_trip = sorted(onebike_durations)[0]
longest_trip = sorted(onebike_durations)[-1]

# Print out the results
print("The shortest trip was " + str(shortest_trip) + " seconds")
print("The longest trip was " + str(longest_trip) + " seconds")

'''
O código acima demonstra como calcular a duração da viagem mais curta e mais longa, utilizando a lista onebike_durations. Ele ordena a lista de durações e seleciona o primeiro e o último elemento, que correspondem à viagem mais curta e mais longa, respectivamente.
'''