try:
    valor = int(input("Informe o valor do saque (mínimo R$10 e máximo R$600): "))
except ValueError:
    print("Entrada inválida. Digite um número inteiro (ex.: 256).")
    exit()

if valor < 10 or valor > 600:
    print("Valor inválido. O valor mínimo é de R$10 e o máximo é de R$600.")
else:
    restante = valor

    notas_100, restante = divmod(restante, 100)
    notas_50, restante = divmod(restante, 50)
    notas_10, restante = divmod(restante, 10)
    notas_5, restante = divmod(restante, 5)
    notas_1 = restante

    partes = []
    if notas_100 > 0:
        partes.append(f"{notas_100} nota{'s' if notas_100 > 1 else ''} de 100")
    if notas_50 > 0:
        partes.append(f"{notas_50} nota{'s' if notas_50 > 1 else ''} de 50")
    if notas_10 > 0:
        partes.append(f"{notas_10} nota{'s' if notas_10 > 1 else ''} de 10")
    if notas_5 > 0:
        partes.append(f"{notas_5} nota{'s' if notas_5 > 1 else ''} de 5")
    if notas_1 > 0:
        partes.append(f"{notas_1} nota{'s' if notas_1 > 1 else ''} de 1")

    if len(partes) == 1:
        frase = partes[0] + "."
    else:
        frase = ", ".join(partes[:-1]) + " e " + partes[-1] + "."

    print(f"Para sacar a quantia de R${valor}, serão fornecidas {frase}")