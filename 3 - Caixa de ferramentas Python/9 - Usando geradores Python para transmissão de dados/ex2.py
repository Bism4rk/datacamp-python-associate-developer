# Define read_large_file()
def read_large_file(file_object):
    """A generator function to read a large file lazily."""

    # Loop indefinitely until the end of the file
    while True:

        # Read a line from the file: data
        data = file_object.readline()

        # Break if this is the end of the file
        if not data:
            break

        # Yield the line of data
        yield data

# Open a connection to the file
with open('world_dev_ind.csv') as file:

    # Create a generator object for the file: gen_file
    gen_file = read_large_file(file)

    # Print the first three lines of the file
    print(next(gen_file))
    print(next(gen_file))
    print(next(gen_file))

'''
O código acima demonstra como criar uma função geradora para ler um arquivo grande de forma preguiçosa (lazy). A função `read_large_file` lê o arquivo linha por linha e usa `yield` para retornar cada linha, permitindo que o arquivo seja processado sem carregar todo o conteúdo na memória de uma só vez. O gerador é utilizado para imprimir as três primeiras linhas do arquivo `world_dev_ind.csv`, mostrando como acessar os dados de forma eficiente.
'''