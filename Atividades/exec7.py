valores = []

print("Digite valores numéricos (digite -1 para encerrar):")

while True:
    try:
        num = int(input("Número: "))
    except ValueError:
        print("Entrada inválida. Digite um número inteiro!")
        continue

    if num == -1:
        break
    valores.append(num)

# Se não digitou nenhum valor válido
if len(valores) == 0:
    print("Nenhum valor foi informado.")
else:
    qtd = len(valores)
    soma = sum(valores)
    media = soma / qtd
    acima_media = sum(1 for v in valores if v > media)

    print("\n=== RESULTADOS ===")
    print(f"Quantidade de valores lidos: {qtd}")
    print("Valores na ordem informada:", valores)
    print("Valores na ordem inversa:", list(reversed(valores)))
    print(f"Soma dos valores: {soma}")
    print(f"Média dos valores: {media:.2f}")
    print(f"Quantidade de valores acima da média: {acima_media}")