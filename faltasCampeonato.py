'''
Faça um programa que percorre uma lista com o seguinte
formato: [['Brasil', 'Italia', [10, 9]], ['Brasil', 'Espanha', [5, 7]],
['Italia', 'Espanha', [7,8]]]. Essa lista indica o número de faltas
que cada time fez em cada jogo. Na lista acima, no jogo
entre Brasil e Itália, o Brasil fez 10 faltas e a Itália fez 9. O
programa deve imprimir na tela:
(a) o total de faltas do campeonato
(b) o time que fez mais faltas
(c) o time que fez menos faltas
'''

# lista <- [['Brasil', 'Itália', [10, 9]], ['Brasil', 'Espanha', [5, 7]], ['Itália', 'Espanha', [7, 8]]
lista = [['Brasil', 'Italia', [10, 9]], ['Brasil', 'Espanha', [5, 7]], ['Italia', 'Espanha', [7, 8]]]
# totalFaltas <- lista[1][3][1] + lista[1][3][2] + lista[2][3][1] + lista[2][3][2] + lista[3][3][1] + lista[3][3][2]
totalFaltas = lista[0][2][0] + lista[0][2][1] + lista[1][2][0] + lista[1][2][1] + lista[2][2][0] + lista[2][2][1]

# IMPRIMA totalFaltas
print(f'O total de faltas do campeonato foi: {totalFaltas}')

# faltasBrasil <- lista[1][3][1] + lista[2][3][1]
faltasBrasil = lista[0][2][0] + lista[1][2][0]
# faltasItalia <- lista[1][3][2] + lista[3][3][1]
faltasItalia = lista[0][2][1] + lista[2][2][0]
# faltasEspanha <- lista[2][3][2] + lista[3][3][2]
faltasEspanha = lista[1][2][1] + lista[2][2][1]

# SE faltasBrasil > faltasEspanha ENTÃO
if faltasBrasil > faltasEspanha:
    # SE faltasBrasil > faltasItália
    if faltasBrasil > faltasItalia:
        # IMPRIMA 'Brasil'
        print(f'O time que fez mais faltas no campeonato foi: Brasil ({faltasBrasil})')
        # SE faltasItalia > faltasEspanha ENTÃO
        if faltasItalia > faltasEspanha:
            # IMPRIMA 'Espanha'
            print(f'O time que fez menos faltas foi: Espanha ({faltasEspanha})')
        # SENÃO
        else:
            # IMPRIMA 'Itália'
            print(f'O time que fez menos faltas foi: Itália ({faltasItalia})')
    # SENÃO
    else:
        # IMPRIMA 'Itália'
        print(f'O time que fez mais faltas no campeonato foi: Itália ({faltasItalia})')
# SENÃO
else:
    # SE faltasEspanha > faltasItalia ENTÃO
    if faltasEspanha > faltasItalia:
        # IMPRIMA 'Espanha'
        print(f'O time que fez mais faltas no campeonato foi: Espanha ({faltasEspanha})')
        # SE faltasItalia > faltasBrasil ENTÃO
        if faltasItalia > faltasBrasil:
            # IMPRIMA 'Brasil'
            print(f'O time que fez menos faltas foi: Brasil ({faltasBrasil})')
        # SENÃO
        else:
            # IMPRIMA 'Itália'
            print(f'O time que fez menos faltas no campeonato foi: Itália ({faltasItalia})')
    # SENÃO
    else:
        # IMPRIMA 'Itália'
        print(f'O time que fez mais faltas no campeonato foi: Itália ({faltasItalia})')
