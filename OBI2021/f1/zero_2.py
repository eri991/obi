n = int(input())
lista = []
for i in range(n):
    x = int(input())
    if x == 0:
        lista.pop()
    else:
        lista.append(x) 
print(sum(lista))