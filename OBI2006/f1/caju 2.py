linhas, colunas, linhas_sub, colunas_sub = list(map(int, input().split()))
matriz = []

for _ in range(linhas):
    matriz.append(list(map(int, input().split())))

maior = 0

for i in range(linhas - linhas_sub + 1):
    for j in range(colunas - colunas_sub + 1):
        submatriz = [linha[j : j + colunas_sub] for linha in matriz[i : i + linhas_sub]]
        soma = sum(sum(linha) for linha in submatriz)
        maior = max(soma, maior)

print(maior)