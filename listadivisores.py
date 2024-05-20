# LEIA num
num = int(input('Digite um número inteiro para verificar a lista de seus divisores:\n'))
# lista <- [1]
lista = [1]
# SE num % 2 = 0 ENTÃO
if num % 2 == 0 and num != 2:
    # ADICIONE 2 à lista
    lista.append(2)
    # PARA i VARIANDO de 3 a (num / 2) - 1
    for i in range(3, (num//2)):
        # SE num % i = 0 ENTÃO
        if num % i == 0:
            # ADICIONE i à lista
            lista.append(i)
    # ADICIONE num / 2 à lista
    lista.append(num//2)
# SENÃO
elif num % 2 == 1:
    # PARA i VARIANDO de 3 a num / 3
    for i in range(3, (num//3) + 1):
        # SE num % i = 0 ENTÃO
        if num % i == 0:
            # ADICIONE i à lista
            lista.append(i)
# ADICIONE num à lista
lista.append(num)
# SE tamanho da lista = 2
if len(lista) == 2:
    # ESCREVA "O número num é primo!"
    print(f'O número {num} é primo!')
# SENÃO
else:
     # ESCREVA lista
     print(f'Divisores de {num}: {lista}')