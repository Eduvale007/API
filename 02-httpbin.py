import requests

#url = 'https://httpbin.org/get'
url = 'https://httpbin.org/post'
data = {
    'pessoa':{
        "nome": "Eduardo",
        "profissao" : "desenvolvedor"
    }
}

params = {
    "dataIni": "2025-01-01",
    "dataFim": "2025-12-31"
}

#response = requests.get(url)
response = requests.post(url, json=data, params=params)
print(response.url)
print(response)
print(response.text)