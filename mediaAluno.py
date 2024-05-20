'''
aluno = str(input("Digite o nome do aluno para calcular sua média:\n"))
# Leia P1
p1 = float(input(f'Digite a primeira nota do(a) {aluno}:\n'))
# Leia P2
p2 = float(input(f'Digite a segunda nota do(a) {aluno}:\n'))
# Leia Trabalho
trab = float(input(f'Digite a nota do trabalho do(a) {aluno}:\n'))
# Leia Participação
part = float(input(f'Digite a nota de participação do(a) {aluno}:\n'))
# Provas <- 3 * P1 + 3 * P2
provas = 3 * (p1 + p2)
# Media <- (Provas + 3 * Trabalho + Participação) / 10
media = (provas + 3 * trab + part) / 10
# Imprima Media
print(f'Media do (a) {aluno}: {media:.2f}')
'''

# Otimizado:
aluno = str(input("Digite o nome do aluno para calcular sua média:\n"))
p1, p2 = map(float, input(f'Digite as 2 notas do(a) {aluno}, separadas por espaço:\n').split())
trab = float(input(f'Digite a nota do trabalho do(a) {aluno}:\n'))
part = float(input(f'Digite a nota de participação do(a) {aluno}:\n'))
print(f'Média do {aluno}: {(3 * (p1 + p2 + trab) + part) / 10:.2f}')
