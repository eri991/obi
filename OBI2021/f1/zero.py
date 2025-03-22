n, lista = int(input()), []
for i in range(n):
    x = int(input())
    lista.append(x) if x != 0 else lista.pop()
print(sum(lista))