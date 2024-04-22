x = int(input())
y = int(input())

if x > y:
    x, y = y, x

soma = 0

if x % 2 != 0 and y % 2 != 0:
    for i in range(x + 2, y - 1, 2):
        soma += i

elif x % 2 == 0 and y % 2 != 0:
    for i in range(x + 1, y - 1, 2):
        soma += i

elif x % 2 == 0 and y % 2 == 0:
    for i in range(x + 1, y, 2):
        soma += i

else:
    for i in range(x + 2, y, 2):
        soma += i

print(soma)
