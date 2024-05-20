# Programa para somar 2 matrizes bidimensionais, com dimensões e elementos já definidos

# Definir matrizes
matriz1 = [[6, 7], [5, 6]]
matriz2 = [[8, 5], [9, 8]]

# Definir matriz que receberá a soma
somaMatriz = [[0, 0], [0, 0]]

# Para cada linha
for i in range(2):
    # Para cada coluna
    for j in range(2):
        # Atribuir a soma dos elementos de dimensão linha x por coluna de cada matriz a linha x coluna
        # da matriz das somas
        somaMatriz[i][j] = matriz1[i][j] + matriz2[i][j]
    # Imprimir linha da matriz de soma
    print(somaMatriz[i])
