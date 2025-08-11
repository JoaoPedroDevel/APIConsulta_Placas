import requests
from requests.auth import HTTPBasicAuth

# Credenciais
username = ""
api_key = "ChaveAPI"

# Endpoint base
url = "https://api.consultarplaca.com.br/v2"

# Dados
dados = {
    "placa": "AAA0000"
}

# Requisição POST
response = requests.post(url, json=dados, auth=HTTPBasicAuth(username, api_key))

# Verifica a resposta
if response.status_code == 200:
    print("Consulta realizada com sucesso:")
    print(response.json())
else:
    print("Erro na consulta:")
    print("Status:", response.status_code)
    print("Mensagem:", response.text)
