def dijkstra(grafo, origem):
    dist = {v: float('inf') for v in grafo}
    dist[origem] = 0
    nao_visitados = set(grafo)
    while nao_visitados:
        vertice_atual = min(nao_visitados, key=lambda v: dist[v])
        nao_visitados.remove(vertice_atual)
        for vizinho, peso in grafo[vertice_atual].items():
            dist[vizinho] = min(dist[vizinho], dist[vertice_atual] + peso)
    return dist
n, m = list(map(int, input().split()))
grafo = {v: {} for v in range(0, n+2)}
for i in range(m):
    s, t, b = list(map(int, input().split()))
    grafo[s][t] = grafo[t][s] = b

print(dijkstra(grafo, 0)[n+1])
