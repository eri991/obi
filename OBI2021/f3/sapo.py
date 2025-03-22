n, m = list(map(int, input().split()))
p = int(input())
pedras = [[0]*100]*100
visitados = [[0]*100]*100
for i in range(p):
    c, l = list(map(int, input().split()))
    pedras[c][l] = 1

sc, sl = list(map(int, input().split()))
rc, rl = list(map(int, input().split()))

def dfs(c, l):
    visitados[c][l] = 1
    for d in range(1, 4):
        if c+d <= n and pedras[c+d][l] and not visitados[c+d][l]:
            dfs(c+d, l)
        if c-d >= 1 and pedras[c-d][l] and not visitados[c-d][l]:
            dfs(c-d, l)
        if l+d <= m and pedras[c][l+d] and not visitados[c][l+d]:
            dfs(c, l+d)
        if l-d >= 1 and pedras[c-d][l] and not visitados[c][l-d]:
            dfs(c, l-d)

dfs(sc, sl)

print(visitados[rc][rl])