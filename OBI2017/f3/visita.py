def dijkstra(grafo, origem):
    dist = {v: float('inf') for v in grafo}
    dist[origem] = 0
    
    nao_visitados = set(grafo)
    
    while nao_visitados:
        vertice_atual = min(nao_visitados, key=lambda v: dist[v])
        
        nao_visitados.remove(vertice_atual)
        
        for vizinho, peso in grafo[vertice_atual].items():
            dist[vizinho] = min([dist[vizinho], dist[vertice_atual] + peso])
    return dist

n, a, b = list(map(int, input().split()))
grafo = {v: {} for v in range(1, n+1)}
for i in range(n-1):
    p, q, d = list(map(int, input().split()))
    grafo[p][q] = grafo[q][p] = d

print(dijkstra(grafo, a)[b])