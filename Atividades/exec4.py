gabarito = ["A", "B", "C", "D", "E", "E", "D", "C", "B", "A"]

maior = 0
menor = 10
total_alunos = 0
soma_notas = 0

while True:
    print(f"Aluno {total_alunos + 1}:")
    acertos = 0

    for i in range(10):
        resposta = input(f"Questão {i+1}: ").strip().upper()
        if resposta == gabarito[i]:
            acertos += 1

    print(f"Você acertou {acertos} de 10 questões.")

    if acertos > maior:
        maior = acertos
    if acertos < menor:
        menor = acertos

    total_alunos += 1
    soma_notas += acertos

    continuar = input("Outro aluno vai fazer a prova? (S/N): ").strip().upper()
    if continuar != "S":
        break

if total_alunos > 0:
    media = soma_notas / total_alunos
    print("\n=== RESULTADOS FINAIS ===")
    print(f"Maior nota: {maior}")
    print(f"Menor nota: {menor}")
    print(f"Total de alunos: {total_alunos}")
    print(f"Média da turma: {media:.2f}")
else:
    print("Nenhum aluno participou.")