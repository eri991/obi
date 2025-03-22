n, lista = int(input()), list(map(int, input().split()))
ops = i = 0
while lista != lista[::-1]:
    if lista[i] < lista[n-1-i]:
        lista[i] += lista[i+1]
        lista.remove(lista[i+1])
        ops += 1
        i -= 1
    elif lista[n-1-i] < lista[i]:
        lista[n-1-i] += lista[n-2-i]
        lista.remove(lista[n-2-i])
        ops += 1
        i -= 1
    i += 1

print(ops)