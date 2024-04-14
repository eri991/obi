n, lista = int(input()), list(map(int, input().split()))
a = b = 0
for i in lista:
    if i == 1:
        a = 1 if a == 0 else 0
    else:
        a = 1 if a == 0 else 0
        b = 1 if b == 0 else 0
print(a)
print(b)