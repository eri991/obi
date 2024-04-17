n, f = list(map(int, input().split()))
matriz, pilha = [], [(0,0)]
for _ in range(n):
    matriz.append(list(map(int, input())))
while pilha:
    i, j = pilha.pop()
    if matriz[i][j] != "*" and matriz[i][j] <= f:
        matriz[i][j] = "*"
        pilha.append((i-1, j)) if i != 0 else ""
        pilha.append((i, j-1)) if j != 0 else ""
        pilha.append((i+1, j)) if i != n-1 else ""
        pilha.append((i, j+1)) if j != n-1 else ""
for i in matriz:
    print("".join([str(j) for j in i]))