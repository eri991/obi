n = int(input())
lista = list(map(int, input().split()))
listaColorida, indexes = [], []

aux = lista.copy()

while 0 in aux:
    indexes.append(aux.index(0))
    aux[aux.index(0)] = "_"

for i in range(len(lista)):
    if lista[i] == -1:
        distancias = []
        for index in indexes:
            distancias.append(abs(i-index))
        listaColorida.append(min(distancias))
    else:
        listaColorida.append(0)

print(" ".join([str(i) for i in listaColorida]))