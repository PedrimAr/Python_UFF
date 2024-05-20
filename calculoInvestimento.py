'''
Faça um programa que calcule o retorno de um investimento
financeiro fazendo as contas mês a mês, sem usar a fórmula de
juros compostos
'''


'''
# LEIA valorInvestido
valorInvestido = float(input('Informe o valor a ser investido mensalmente no período de um ano:\n'))
# LEIA jurosMensal
jurosMensal = float(input('Informe, agora, a taxa de juros mensal que incidirá sobre o investimento (apenas o número inteiro)\n')) /100
# valorFinal <- 0.0
valorFinal = 0.0
# PARA i VARIANDO de 1 a 12
for i in range(1, 13):
    # valorFinal += valorInvestido
    valorFinal += valorInvestido
    # valorFinal += valorFinal x (jurosMensal/100)
    valorFinal += valorFinal * jurosMensal
# ESCREVA 'Saldo do investimento após 1 ano: valorFinal'
print(f'Saldo do investimento após 1 ano:\n{valorFinal:.2f}')
'''

'''
OTIMIZADO
'''

# LEIA valorInvestido
valorInvestido = float(input('Informe o valor a ser investido mensalmente no período de um ano:\n'))
# LEIA jurosMensal
jurosMensal = float(input('Informe, agora, a taxa de juros mensal que incidirá sobre o investimento (apenas o número inteiro)\n')) /100
# valorFinal <- 0.0
valorFinal = 0.0
# ok <- 'sim'
ok = 'sim'
# j <- 1
j = 1
# ENQUANTO sim FAÇA
while ok == 'sim':
    # PARA i VARIANDO de 1 a 12
    for i in range(1, 13):
        # valorFinal += valorInvestido
        valorFinal += valorInvestido
        # valorFinal += valorFinal x (jurosMensal/100)
        valorFinal += valorFinal * jurosMensal
    # ESCREVA 'Saldo do investimento após j ano: valorFinal'
    print(f'Saldo do investimento após {j} ano(s):\n{valorFinal:.2f}')
    # LEIA ok
    ok = input('Deseja calcular mais um ano?\n').lower()
    # j <- j + 1
    j += 1
