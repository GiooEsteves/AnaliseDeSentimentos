import requests

def fetchDataFromApi(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Falha em pegar o dado da API. Status code: {response.status_code}")
    