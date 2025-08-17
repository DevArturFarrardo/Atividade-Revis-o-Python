import requests

cep = input('Digite o CEP do destino: ')
url = f'https://viacep.com.br/ws/{cep}/json/'
response = requests.get(url)
dados = response.json()

if cep[0] != '0':
    zona = 'Fora de São Paulo'
elif cep[1] == '1':
    zona = 'Centro de São Paulo'
elif cep[1] == '2':
    zona = 'Zona Norte de São Paulo' 
elif cep[1] == '3':
    zona = 'Zona Leste de São Paulo'
elif cep[1] == '4':
    zona = 'Zona Sul de São Paulo'
elif cep[1] == '5':
    zona = 'Zona Oeste de São Paulo'
elif cep[1] == '6':
    zona = 'Zona Oeste de São Paulo'
elif cep[1] == '7':
    zona = 'Zona Oeste de São Paulo'
elif cep[1] == '8':
    zona = 'Zona Leste de São Paulo'
elif cep[1] == '9':
    zona = 'Zona Leste de São Paulo'

print(f'Bairro destino: {dados['bairro']}, {zona}')
...