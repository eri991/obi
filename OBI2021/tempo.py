n = int(input())
vacuo = [False]*101
tempo = [0]*101
amigos = []
intervalo = 0
for i in range(n):
    evento, valor = input().split()
    valor = int(valor)
    if evento == "R":
        if valor not in amigos:
            amigos.append(valor)
        vacuo[valor] = True
        intervalo = 1
    if evento == "E":
        vacuo[valor] = False
        intervalo = 1
    if evento == "T":
        intervalo = valor-1
    for i in range(len(vacuo)):
        if vacuo[i] == True:
            tempo[i] += intervalo
amigos.sort()
for i in amigos:
    if vacuo[i] == True:
        print(f"{i} -1")
    else:
        print(f"{i} {tempo[i]}")