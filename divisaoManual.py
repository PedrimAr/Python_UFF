'''
Faça um programa que leia dois valores x e y, e calcula o
valor de x dividido por y, além do resto da divisão. Não é
permitido usar as operações de divisão e resto de divisão
do Python (use apenas soma e subtração).
'''

# LEIA x
dividendo = int(input('Digite o dividendo:\n'))
# LEIA y
divisor = int(input('Digite o divisor:\n'))
# quociente <- 1
quociente = 1
# ENQUANTO (x - y) > y FAÇA
while (dividendo - divisor) >= divisor:
    # quociente <- q + 1
    quociente += 1
    dividendo -= divisor
# resto <- x - y
resto = dividendo - divisor
# ESCREVA 'x dividido por y é igual a quociente, com resto resto.'
print(f'{(dividendo - resto) * quociente + resto} dividido por {divisor} é igual a {quociente}, com resto {resto}.')

