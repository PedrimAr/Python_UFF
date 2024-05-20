'''
print('-CÁLCULO DO PESO IDEAL-')
# Leia ALtura
altura = int(input('Digite sua altura em cm:\n')) / 100
# Leia Gênero
genero = str(input('Digite seu gênero, masculino ou feminino:\n'))
# Se o Gênero for masculino, então
    Peso Ideal <- (72.7 * Altura) - 58
if genero.strip().lower() == 'masculino':
    pesoIdeal = (72.7 * altura) - 58
# Senão
    Peso Ideal <- (62.1 * Altura) - 44.7
else:
    pesoIdeal = (62.1 * altura) - 44.7
# Imprima Peso Ideal
print(f'Seu peso ideal é: {pesoIdeal:.2f}')
'''

# Otimizado
i = 0
print('-CÁLCULO DO PESO IDEAL-')
altura = int(input('Digite sua altura em cm:\n')) / 100
while i ==0:
    genero = str(input('Digite seu gênero, masculino ou feminino:\n'))
    if genero.strip().lower() == 'masculino':
        print(f'Seu peso ideal é: {(72.7 * altura) - 58:.2f}')
        i += 1
    elif genero.strip().lower() == 'feminino':
        print(f'Seu peso ideal é: {(62.1 * altura) - 44.7:.2f}')
        i += 1
    else:
        print(f'Gênero não reconhecido, digite novamente, por favor!')
