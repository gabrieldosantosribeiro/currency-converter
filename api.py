import os
import requests
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Pega a chave da API
API_KEY = os.getenv('API_KEY')

# Busca a taxa de câmbio entre duas moedas
def buscar_cotacao(moeda_origem, moeda_destino):
    url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD'

    response = requests.get(url)
    rates =  response.json()['conversion_rates']
    cotacao = rates[moeda_destino] / rates[moeda_origem]

    return cotacao
