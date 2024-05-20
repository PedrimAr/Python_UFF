n = int(input())
m = int(input())
matriz1 = []
matriz2 = []
somaMatriz = []

for i in range(n):
    linha1 = []
    linha2 = []
    linhaSoma = []
    for j in range(m):
        linha1.append(int(input()))
        linha2.append(int(input()))
        linhaSoma.append(linha1[j] + linha2[j])
    matriz1.append(linha1)
    matriz2.append(linha2)
    somaMatriz.append(linhaSoma)

for i in range(n):
    print(matriz1[i])

print()

for i in range(n):
    print(matriz2[i])

print()

for i in range(n):
    print(somaMatriz[i])
