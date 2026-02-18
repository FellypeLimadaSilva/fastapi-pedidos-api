import requests

headers = {
    "Authorization": "Bearer COLE_AQUI_O_REFRESH_TOKEN_JWT"
}

requisicao = requests.get("http://127.0.0.1:8000/auth/refresh", headers=headers)
print(requisicao)
print(requisicao.json())
