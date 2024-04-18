n, m = list(map(int, input().split()))
i, r = list(map(int, input().split()))
infectados = [i]
for reuniao in range(1, m+1):
    lista = list(map(int, input().split()))
    if reuniao < r:
        continue
    else:
        lista = lista[1:]
        for infectado in infectados:
            if infectado in lista:
                for i in lista:
                    infectados.append(i) if i not in infectados else ""
print(len(infectados))