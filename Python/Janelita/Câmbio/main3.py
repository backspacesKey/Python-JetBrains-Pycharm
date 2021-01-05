import requests
key = input('Insira a sua chave do HG Brasil: ')
request = requests.get(f'https://api.hgbrasil.com/finance/quotations?key={key}&format=debug')

moeda = request.json()

print("Dólar: {}".format(moeda))
