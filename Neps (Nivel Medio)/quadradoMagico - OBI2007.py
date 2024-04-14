n = int(input())
colunas, linhas, diagonais, diagonal = [], [], [], []
for i in range(n):
    linhas.append(list(map(int, input().split())))
for x in range(n):
    coluna = []
    for y in range(n):
        coluna.append(linhas[y][x])
    colunas.append(coluna)
    diagonal.append(linhas[x][x])
diagonais.append(diagonal)
diagonal = []
for y in range(n):
    diagonal.append(linhas[y][(len(linhas)-1)-y])
diagonais.append(diagonal)

soma = sum(linhas[0])
quebra = False
for x in [linhas, colunas, diagonais]:
    for i in x:
        if sum(i) != soma:
            quebra = True
            break
    if quebra:
        print(-1)
        break

if quebra == False:
    print(soma)