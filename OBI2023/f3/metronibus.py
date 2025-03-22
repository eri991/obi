n, k1, k2, p = list(map(int, input().split()))
# ligacoes, ligacoes onibus, ligacoes metro, preço
grafo = {v : {} for v in range(1, n+1)}
for i in range(k1):
    v, u = list(map(int, input().split()))
    grafo[v][u] = grafo[u][v] = ("onibus")
for j in range(k2):
    x, y = list(map(int, input().split()))
    grafo[x][y] = grafo[x][y] = ("metro")

a, b = list(map(int, input().split()))


def bfs(inicio, objetivo):
    dist = {v : float('inf') for v in grafo}
    dist[inicio] = 0
    fila = []
    fila += grafo[inicio]
    visitados = []
    transporte_atual = ""
    while fila:
        pessoa = fila.pop(0)
        if pessoa == objetivo:
            return dist[pessoa]
        if pessoa not in visitados:
            for vizinho, transporte in grafo[pessoa].items():
                if transporte_atual == "" or transporte_atual == transporte:
                    fila += grafo[vizinho]
                else:
                    dist[vizinho] = min(dist[vizinho], dist[pessoa] + p)
                    fila += grafo[vizinho]
    return -1

print(bfs(a, b))