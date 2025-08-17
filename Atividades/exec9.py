import requests
from forex_python.converter import CurrencyCodes

moeda = input('Digite a sigla da moeda principal: ')
moeda_conversora = input('Digite a sigla da moeda convertida: ')
url = f'https://api.exchangerate-api.com/v4/latest/{moeda}'
response = requests.get(url)
json_api = response.json()
conversor_nome = CurrencyCodes()
print(f'A moeda {conversor_nome.get_currency_name(moeda)} vale {json_api['rates'][moeda_conversora]} {conversor_nome.get_currency_name(moeda_conversora)}')
...