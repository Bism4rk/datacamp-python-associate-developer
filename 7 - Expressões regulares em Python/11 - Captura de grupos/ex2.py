# Import re
import re

flight = "Subject: You are now ready to fly. Here you have your boarding pass IB3723 AMS-MAD 06OCT"

# Write regex to capture information of the flight
regex = r"([A-Z]{2})(\d{4})\s([A-Z]{3})-([A-Z]{3})\s(\d{2}[A-Z]{3})"

# Find all matches of the flight information
flight_matches = re.findall(regex, flight)
    
#Print the matches
print("Airline: {} Flight number: {}".format(flight_matches[0][0], flight_matches[0][1]))
print("Departure: {} Destination: {}".format(flight_matches[0][2], flight_matches[0][3]))
print("Date: {}".format(flight_matches[0][4]))

'''
O código acima demonstra como usar expressões regulares em Python para capturar grupos específicos de texto, como informações de voo em uma string. A regex `r"([A-Z]{2})(\d{4})\s([A-Z]{3})-([A-Z]{3})\s(\d{2}[A-Z]{3})"` é usada para identificar e extrair o código da companhia aérea, número do voo, aeroporto de partida, aeroporto de destino e data do voo. A função `re.findall()` retorna todas as correspondências encontradas, que são então impressas no console.
'''