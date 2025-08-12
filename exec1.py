# 1. Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# • até 20 litros: desconto de 3% por litro
# • acima de 20 litros: desconto de 5% por litro
# Gasolina:
# • até 20 litros: desconto de 4% por litro
# • acima de 20 litros: desconto de 6% por litro
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado
# da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente
# sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

qtd_litros = float(input("Digite a quantidade de litros de combustivel que deseja abastecer: "))
tipo_combustivel = str(input("Digite se é Alcool ou Gasolina: "))
valor_final = 0

if tipo_combustivel == "alcool":
    preco_combustivel = 1.90
    valor_final = qtd_litros * preco_combustivel
    if qtd_litros > 20:
        valor_final * 0.95
    else:
        valor_final * 0.97

elif tipo_combustivel == "gasolina":
    preco_combustivel = 2.50
    valor_final = qtd_litros * preco_combustivel
    if qtd_litros > 20:
        valor_final * 0.94
    else:
        valor_final * 0.96

else:
    print(str(input("Selecione gasolina ou alcool: ")))

print(valor_final)
