# LEIA A
a = int(input('Digite um número para ver sua tabuada: '))
print(f'- TABUADA DE {a}')
# ESCREVA "A x 1 = A"
print(f'{a} x 1 = {a}')
# PARA i VARIANDO de 2 a 10
for i in range(2, 11):
    # ESCREVA "A x i = A * i"
    print(f'{a} x {i} = {a * i}')
