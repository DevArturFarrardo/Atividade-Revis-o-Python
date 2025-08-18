# 3. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina
# ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à
# tabela abaixo:

# 1

# Atividade de Revisão em Python - IMPACTA
# Média de Aproveitamento Conceito
# Entre 9.0 e 10.0 A
# Entre 7.5 e 9.0 B
# Entre 6.0 e 7.5 C
# Entre 4.0 e 6.0 D
# Entre 4.0 e zero e
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a
# mensagem


nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = int(nota1 + nota2)/2
nota_aluno = 0
conceito = 0

if media > 9:
    nota_aluno = 'A'
    conceito = 'Aprovado'

elif media > 7.5 and media <= 9:
    nota_aluno = 'B'
    conceito = 'Aprovado'

elif media > 6 and media <= 7.5:
    nota_aluno = 'C'
    conceito = 'Aprovado'

elif media > 4 and media <= 6.0:
    nota_aluno = 'D'
    conceito = 'Reprovado'

elif media <= 4 and media >= 0:
    nota_aluno = 'E'
    conceito = 'Reprovado'

print(f'Sua nota é {nota_aluno} com {media} de média. \nSituação: {conceito}')