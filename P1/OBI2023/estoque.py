m, n = list(map(int, input().split()))
matriz, vendidos = [], 0
for i in range(m):
    matriz.append(list(map(int, input().split())))
for i in range(int(input())):
    i, j = list(map(int, input().split()))
    i, j = i-1, j-1
    if matriz[i][j] > 0:
        matriz[i][j] -= 1
        vendidos += 1
print(vendidos)