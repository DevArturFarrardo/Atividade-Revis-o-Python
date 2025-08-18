# 5. O cardápio de uma lanchonete é o seguinte:
# Especificação Código Preço
# Cachorro Quente 100 R$ 1,20
# Bauru Simples 101 R$ 1,30
# Bauru com ovo 102 R$ 1,50
# Hambúrguer 103 R$ 1,20
# Cheeseburguer 104 R$ 1,30
# Refrigerante 105 R$ 1,00
# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule
# e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido.
# Considere que o cliente deve informar quando o pedido deve ser encerrado.


cardapio = {
    100: ("Cachorro Quente", 1.20),
    101: ("Bauru Simples", 1.30),
    102: ("Bauru com Ovo", 1.50),
    103: ("Hambúrguer", 1.20),
    104: ("Cheeseburguer", 1.30),
    105: ("Refrigerante", 1.00)
}

total = 0
print('Bem vindo à lanchonete!! Aqui está nosso cardápio, aproveite!\n' + '-'*30)
print(f'{"Código":<6} {"Produto":<20} {"Preço":>6}')
print('-'*30)

for codigo, (nome, preço) in cardapio.items():
    print(f'{codigo:<6} {nome:<20} R$ {preço:>5.2f}')

print('-'*30)

fazendo_pedido = True

while fazendo_pedido == True:
    print('-'*30)
    print('Realizando pedido - Para cancelar digite "cancelar"\n' + '-'*30)
    codigo = input('Digite o código do produto: ')

    if codigo.lower() == 'cancelar':
        fazendo_pedido = False
        print('Pedido cancelado')
        break

    if not codigo.isdigit():
        print("Código inválido! Tente novamente.\n" + '-'*30)
        continue

    codigo = int(codigo)

    if codigo not in cardapio:
        print("Código inválido! Tente novamente.\n" + '-'*30)
        continue

    quantidade = input("Digite a quantidade: ")

    if not quantidade.isdigit() or int(quantidade) <= 0:
        print("Quantidade inválida! Tente novamente.\n" + '-'*30)
        continue

    quantidade = int(quantidade)
    print('-'*30)
    nome, preco = cardapio[codigo]
    valor = preco * quantidade
    total += valor
    print(f"{quantidade}x {nome:<20} = R$ {valor:>6.2f}")

print(f'\n{"Total:":<27} R$ {total:.2f}')
