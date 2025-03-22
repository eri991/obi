linhas, colunas, linhas_sub, colunas_sub = list(map(int, input().split()))
matriz = []
for _ in range(linhas):
    matriz.append(list(map(int, input().split())))

submatrizes = []
for i in range(linhas - linhas_sub + 1):
    for j in range(colunas - colunas_sub + 1):
        submatriz = [linha[j:j + colunas_sub] for linha in matriz[i:i + linhas_sub]]
        submatrizes.append(submatriz)

maior = 0
for submatriz in submatrizes:
    soma = sum(sum(i) for i in submatriz)
    maior = max(maior, soma)

print(maior)