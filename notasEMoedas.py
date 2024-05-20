valor = float(input('Digite um valor monetário com duas casas decimais: '))

n100 = int(valor // 100)
n050 = int((valor % 100) // 50)
n020 = int(((valor % 100) % 50) // 20)
n010 = int((((valor % 100) % 50) % 20) // 10)
n005 = int(((((valor % 100) % 50) % 20) % 10) // 5)
n002 = int((((((valor % 100) % 50) % 20) % 10) % 5) // 2)

m1_00 = int(((((((valor % 100) % 50) % 20) % 10) % 5) % 2) // 1)
m0_50 = int((((((((valor % 100) % 50) % 20) % 10) % 5) % 2) % 1) // 0.5)
m0_25 = int(((((((((valor % 100) % 50) % 20) % 10) % 5) % 2) % 1) % 0.5) // 0.25)
m0_10 = int((((((((((valor % 100) % 50) % 20) % 10) % 5) % 2) % 1) % 0.5) % 0.25) // 0.1)
m0_05 = int(((((((((((valor % 100) % 50) % 20) % 10) % 5) % 2) % 1) % 0.5) % 0.25) % 0.1) // 0.05)
m0_01 = int((((((((((((valor % 100) % 50) % 20) % 10) % 5) % 2) % 1) % 0.5) % 0.25) % 0.1) % 0.05) // 0.01)

print(f'NOTAS:\n{n100} nota (s) de R$ 100.00\n{n050} nota (s) de R$ 50.00\n{n020} nota (s) de R$ 20.00\n{n010} nota (s) de R$ 10.00\n{n005} nota (s) de R$ 5.00\n{n002} nota (s) de R$ 2.00')
print(f'MOEDAS:\n{m1_00} moeda (s) de R$ 1.00\n{m0_50} moeda (s) de R$ 0.50\n{m0_25} moeda (s) de R$ 0.25\n{m0_10} moeda (s) de R$ 0.10\n{m0_05} moeda (s) de R$ 0.05\n{m0_01} moeda (s) de R$ 0.01')
