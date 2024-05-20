# LEIA massa
massa = float(input('Informe sua massa em KG:\n'))
# LEIA altura
altura = float(input('Informe sua altura em metros:\n')) ** 2
# imc <- massa / altura
imc = massa / altura
# SE imc < 18,5 ENTÃO
if  imc < 18.5:
    # ESCREVA "Seu IMC é imc e você está abaixo do peso!"
    print(f'Seu IMC é {imc:.2f} e você está abaixo do peso!')
# SENÃO SE 18.6 <= imc and <= 24.9 ENTÃO
elif 18.6 <= imc <= 24.9:
    # ESCREVA "Seu IMC é imc e você está sáudavel!"
    print(f'Seu IMC é {imc:.2f} e você está saudável!')
# SENÃO SE 25.0 <= imc <= 29.9 ENTÃO
elif 25 <= imc <= 29.9:
    # ESCREVA "Seu IMC é imc e você está com peso em excesso!"
    print(f'Seu IMC é {imc:.2f} e você está com peso em excesso!')
# SENÃO SE 30.0 <= imc <= 34.9 ENTÃO
elif 30 <= imc <= 34.9:
    # ESCREVA "Seu IMC é imc e você está com Obesidade Grau I!"
    print(f'Seu IMC é {imc:.2f} e você está com Obesidade Grau I!')
# SENÃO SE 35.0 <= imc <= 39.9 ENTÃO
elif 35 <= imc <= 39.9:
    # ESCREVA "Seu IMC é imc e você está com Obesidade Grau II (severa)!"
    print(f'Seu IMC é {imc:.2f} e você está com Obesidade Grau II (severa)!')
# SENÃO
else:
    # ESCREVA "Seu IMC é imc e você está com Obesidade Grau III (mórbida)!"
    print(f'Seu IMC é {imc:.2f} e você está com Obesidade Grau III (mórbida)!')
