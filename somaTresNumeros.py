'''
print('-SOMA DE 3 NÚMEROS INTEIROS-')
# Leia A
a = int(input('Digite o primeiro número a ser somado:\n'))
# Leia B
b = int(input('Digite o segundo número a ser somado:\n'))
# Leia C
c = int(input('Digite o terceiro número a ser somado:\n'))
# Soma <- A + B + C
soma = a + b + c
# Imprima soma
print(f'SOMA: {a} + {b} + {c} = {soma}')
'''

# Otimizado:
print('-SOMA DE 3 NÚMEROS INTEIROS-')
a, b, c = map(int, input('Digite os 3 números a serem somados, separados por espaço:\n').split())
print(f'Soma: {a} + {b} + {c} = {a + b + c}')
