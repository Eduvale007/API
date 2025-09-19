import requests
from pprint import pprint
from requests.exceptions import HTTPError


def obter_request(url, params=None):
    '''Faz uma requisição GET e retorna a resposta em JSON'''
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except HTTPError as e:
        print(f'Erro no request: {e}')
        return None


def busca_id_estado():
    '''Obtém um dicionário de estado no formato {id_estado: nome_estado}''' 
    url = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados'
    dados_estado = obter_request(url, params={"view": "nivelado"}) or []
    return {estado["UF-id"]: estado["UF-nome"] for estado in dados_estado}

    
def frequencia_nome(name):
    '''Obtém um dicionário de frequência de um nome por estado no formato {id_estado: frequencia}'''  
    url = f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{name}' 
    dados_frequencia = obter_request(url, params={"groupBy": "UF"}) or []
    return {int(dado["localidade"]): dado["res"][0]["proporcao"] for dado in dados_frequencia}

def main(name):
    dict_estados = busca_id_estado()
    dict_frequencias = frequencia_nome(name)
    print(f'=== Frequência do nome {name} nos Estados (por 100.000 habitantes) ===')
    for id_estado, frequencia in sorted(dict_frequencias.items(), key=lambda item: item[1], reverse=True):
        print(f"-> {dict_estados.get(id_estado, 'Desconhecido')}: {frequencia}")


if __name__ == '__main__':
    main('Eduardo')