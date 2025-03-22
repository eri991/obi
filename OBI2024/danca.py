matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
q = int(input())
# quant. de trocas
for _ in range(q):
    sentido, x, y = input().split()
    # linha ou coluna, onde é pra ir, onde tá
    x, y = int(x)-1, int(y)-1
    # pegando o indice certo
    if sentido == "L":
        matriz[y], matriz[x] = matriz[x], matriz[y]
    else:
        for i in range(len(matriz)):
            matriz[i][y], matriz[i][x] = matriz[i][x], matriz[i][y]

for i in matriz:
    for j in i:
        print(j, end=" ")
    print()