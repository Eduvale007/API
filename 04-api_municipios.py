import requests

from pprint import pprint


url = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados'

params = {
    "view": "nivelado"
}

response = requests.get(url, params=params)

try:
    response.raise_for_status()
except requests.HTTPError as e:
    print(f'Erro no request: {e}')
    resultado = None
else:
    resultado = response.json()
    pprint(resultado)