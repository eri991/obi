n, lista = int(input()), list(map(int, input().split()))
ops = i = 0
while True:
    if lista == lista[::-1]:
        print(ops)
        break
    else:
        if lista[i] < lista[len(lista)-1-i]:
            lista[i] += lista[i+1]
            lista.remove(lista[i+1])
            ops += 1
            i -= 1
        elif lista[len(lista)-1-i] < lista[i]:
            lista[len(lista)-1-i] += lista[len(lista)-2-i]
            lista.remove(lista[len(lista)-2-i])
            ops += 1
            i -= 1
    i += 1