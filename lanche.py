codigo, quantidade = input("Digite dois valores inteiros correspondentes, primeiro, ao código do produto, sendo esse entre 1 e 5, e depois, à quantidade do mesmo, separados por um espaço: "). split()
codigo = int(codigo)
quantidade = int(quantidade)
valor = 0
if codigo == 1:
    valor = quantidade * 4
    print(f'Total: R$ {valor:.2f}')
elif codigo == 2:
    valor = quantidade * 4.5
    print(f'Total: R$ {valor:.2f}')
elif codigo == 3:
    valor = quantidade * 5
    print(f'Total: R$ {valor:.2f}')
elif codigo == 4:
    valor = quantidade * 2
    print(f'Total: R$ {valor:.2f}')
elif codigo == 5:
    valor = quantidade * 1.5
    print(f'Total: R${valor:.2f}')
else:
    print(f'O codigo {codigo} não está entre 1 e 5')
