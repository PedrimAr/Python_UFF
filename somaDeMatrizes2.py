# Programa para somar 2 matrizes bidimensionais, com dimensões e elementos a receber do console
# E imprimir apenas a soma

# Ler as dimensões das matrizes
n = int(input())
m = int(input())

# Definir matriz de soma
somaMatriz = []

# Para cada linha
for i in range(n):
    # Definir linha temporária
    linha = []

    # Para cada coluna
    for j in range(m):
        # Ler os valores de cada matriz referentes aos elementos ixj
        matriz1 = int(input())
        matriz2 = int(input())
        # Adicionar a soma dos dois valores à linha temporária
        linha.append(matriz1 + matriz2)
    # Adicionar a linha temporária à matriz de soma
    somaMatriz.append(linha)

# Para cada linha
for i in range(n):
    # Imprimir a linha da matriz de soma
    print(somaMatriz[i])
