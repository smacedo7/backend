import requests

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

arquivo = requests.get(url)
print(arquivo)

