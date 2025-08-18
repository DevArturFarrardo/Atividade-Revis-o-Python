# 6. Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
# • Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
# • Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
# • A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do
# percentual do ano anterior.
# Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere
# o programa permitindo que o usuário digite o salário inicial do funcionário.

from datetime import datetime

salario_inicial = 1000
percentual = 0.015
aumento = salario_inicial * percentual
salario_atual = 0

def ano_atual():
    return datetime.now().year

hoje = ano_atual()
contagem_tempo = hoje - 1996

for anos in range (1,contagem_tempo):
    percentual = percentual*2
    aumento = salario_inicial * percentual
    salario_atual += aumento

print(f'O salário atual é de R$ {salario_atual:.2f}')