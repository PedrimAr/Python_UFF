m = int(input())
p = 1

for i in range(2, 101):
    n = int(input())
    if n > m:
        m = n
        p = i

print(m)
print(p)
