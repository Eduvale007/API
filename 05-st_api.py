import requests
import pandas as pd
import streamlit as st
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


def frequencia_nome(name):
    '''Obtém um dicionário de frequência de um nome por década no formato {década: quantidade}'''  
    url = f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{name}' 
    dados_nome = obter_request(url) or []
    #return {dados["periodo"]: dados["frequencia"] for dados in dados_nome[0].get("res", [])}
    dados_dict = {dados["periodo"]: dados["frequencia"] for dados in dados_nome[0].get("res", [])}
    df = pd.DataFrame.from_dict(dados_dict, orient="index")
    return df

import streamlit as st

def main():
    st.title("Web App API")
    st.header("Dados da API do IBGE")
    
    in_name = st.text_input("Digite um nome: ")  
    if not in_name:
        st.stop()
    
    df = frequencia_nome(in_name)  # Assuming this function returns a DataFrame

    col1, col2 = st.columns([0.3, 0.7])
    
    with col1:
        st.write("Frequência por década")
        st.dataframe(df)
    
    with col2:
        st.write("Série temporal")
        st.line_chart(df)
    
    # print(frequencia_nome(in_name))  # Optional for debugging

if __name__ == '__main__':
    main()