nome, salario, vendas = input('Digite o primeiro nome do vendedor, seu salário fixo e o seu valor de vendas no mês, separados por 1 espaço: ').split()
print(f'TOTAL = R$ {(float(salario) + float(vendas) * 15/100):.2f}')
