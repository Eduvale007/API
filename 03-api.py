import requests
from pprint import pprint

nome = input('Digite um nome para pesquisa:\n')
url = f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}'
response = requests.get(url)

try:
    response.raise_for_status()
except requests.HTTPError as e:
    print(f'Erro no request: {e}')
    resultado = None
else:
    resultado = response.json()
    pprint(resultado[0]['res'])