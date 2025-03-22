n = int(input())
lista = []
for i in range(n):
    lista.append(int(input()))
lista.sort(reverse=True)
for i in range(n//3):
    lista.pop()

print(sum(lista))