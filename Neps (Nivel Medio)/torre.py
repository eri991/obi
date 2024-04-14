n = int(input())
linhas = []
colunas = []
for i in range(n):
    linhas.append(list(map(int, input().split())))
for x in range(n):
    coluna = []
    for y in range(n):
        coluna.append(linhas[y][x])
    colunas.append(coluna)
maior = 0
peso = 0

for x in linhas:
    for y in colunas:
        peso += sum(x) + sum(y) - linhas[linhas.index(x)][colunas.index(y)]*2
        maior = peso if peso > maior else maior
        peso = 0

print(maior)