'''
Faça um programa que leia um número inteiro de 5 dígitos e indique se ele é palíndromo
'''
# i <- 0
i = 0
# ENQUANTO i = 0
while i == 0:
    # LEIA num
    num = input("Digite um número inteiro de 5 dígitos para avaliar se é palíndromo:\n")
    # SE tamanho de num != 5 ou não é inteiro ENTÃO
    if len(num) != 5 or "." in num:
        # ESCREVA "O número digitado não é inteiro ou não possui 5 dígitos"
        print(f'O número digitado {num} não é inteiro ou não possui 5 dígitos. Tente novamente!')
    # SENÃO
    else:
        # i <- i + 1
        i += 1
boolean = True
# PARA j variando de 0 a 1
for j in range(0, 2):
    # SE num[j] != num[-j - 1] ENTÃO
    if num[j] != num[-j -1]:
        # bool <- false
        boolean = False
        i = 10
if boolean:
    # ESCREVA "O número inteiro num é palíndromo!"
    print(f'O número inteiro {num} é palíndromo!')
else:
    print(f'O número inteiro {num} não é palíndromo!')
