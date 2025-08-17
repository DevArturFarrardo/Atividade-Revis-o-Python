import requests

pais = input('Digite o nome do país que deseja saber as informações:')
url = f'https://restcountries.com/v3.1/name/{pais}'
response = requests.get(url)
json_api = response.json()
nome_do_pais = json_api[0]['name']['common']
print(f'Nome do país: {nome_do_pais}')
linguagens = list(json_api[0]['languages'].values())
print(f'Lingua do país: {linguagens[0]}')
regiao = json_api[0]['region']
print(f'Regiao do país: {regiao}')
sub_regiao = json_api[0]['subregion']
print(f'Subregiao do país: {sub_regiao}')
capital = json_api[0]['capital']
print(f'Capital do pais: {capital[0]}')
sigla_moeda = list(json_api[0]['currencies'].keys())
print(f'Sigla da moeda do pais: {sigla_moeda[0]}')
simbolo_moeda = json_api[0]['currencies'][sigla_moeda[0]]['symbol']
nome_moeda = json_api[0]['currencies'][sigla_moeda[0]]['name']
print(f'Simbolo da moeda do pais: {simbolo_moeda}')
print(f'Nome da moeda do pais: {nome_moeda}')

try:
    for border in json_api[0]['borders']:
        print('Paises que fazem fronteira:')
        print(border)
except:
    print('Pais não faz fronteiras')