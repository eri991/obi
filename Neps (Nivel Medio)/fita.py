n, lista = int(input()), input().split()
indexes = [index for index, num in enumerate(lista) if num == "0"]
listaColorida = [min(abs(index-indexZero) if abs(index-indexZero) < 9 else 9 for indexZero in indexes) for index in range(n)]
for i in listaColorida:
    print(i, end=" ")