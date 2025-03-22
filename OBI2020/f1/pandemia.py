n, m = list(map(int, input().split()))
i, r = list(map(int, input().split()))
infectados = [i]
for reuniao in range(1, m+1):
    lista = list(map(int, input().split()))
    if reuniao < r:
        continue
    else:
        lista = lista[1:]
        if not set(infectados).isdisjoint(lista):
            infectados = list(set(infectados + lista))
print(len(infectados))