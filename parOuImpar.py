# Ler o valor de n
n = int(input())
# Para cada conjunto de testes
t = 1
while n != 0:
    # Ler o nome dos participantes
    print(f'Teste {t}')
    nome_par = input()
    nome_impar = input()
    # Para cada uma das n partidas no conjunto de testes atual
    for _ in range(1, n):
        # Ler a quantidade de dedos informados por cada participante
        dedos_par, dedos_impar = map(int, input().split())
        # Apontar o primeiro participante como vencedor, caso a soma de dedos for par
        if (dedos_par + dedos_impar) % 2 == 0:
            print(nome_par)
        # Caso contrário, apontar o segundo participante como vencedor
        else:
            print(nome_impar)
    print()
    t += 1
    n = int(input())