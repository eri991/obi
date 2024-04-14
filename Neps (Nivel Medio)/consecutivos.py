n = int(input())
lista = list(map(int, input().split()))
ultimo = lista[0]
contadores = []
contador = 0
for i in lista:
    if i == ultimo:
        contador += 1
    else:
        contadores.append(contador)
        ultimo = i
        contador = 1
if contador:
    contadores.append(contador)
print(max(contadores))