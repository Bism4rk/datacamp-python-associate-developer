feature_names = ['CountryName', 'CountryCode', 'IndicatorName', 'IndicatorCode', 'Year', 'Value']
row_vals = ['Arab World', 'ARB', 'Adolescent fertility rate (births per 1,000 women ages 15-19)', 'SP.ADO.TFRT', '1960', '133.56090740552298']

# Zip lists: zipped_lists
zipped_lists = zip(feature_names, row_vals)

# Create a dictionary: rs_dict
rs_dict = dict(zipped_lists)

# Print the dictionary
print(rs_dict)

'''
O código acima demonstra como criar um dicionário a partir de duas listas: uma contendo os nomes das características e outra contendo os valores correspondentes. A função `zip` combina as duas listas em pares, e a função `dict` converte esses pares em um dicionário. O resultado é um dicionário onde cada chave é um nome de característica e cada valor é o valor correspondente para aquela característica.
'''