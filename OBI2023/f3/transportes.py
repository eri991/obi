n, m, k = [int(x) for x in input().split()]
# numero de nós, número de caminhos, quantidade de transportes
transportes = list(enumerate([int(x) for x in input().split()], 1))
#[(sistema, peso), (sistema2, peso2)]

grafo = {v : {} for v in range(1, n+1)}
# {nó : {vizinho : transporte}}
for i in range(m):
    v, u, tipo_transporte = [int(x) for x in input().split()]
    grafo[v][u] = grafo[u][v] = tipo_transporte
a, b = [int(x) for x in input().split()]

def dijkstra(grafo, origem):
    dist = {v : float('inf') for v in grafo}
    dist[origem] = 0
    
    nao_visitados = set(grafo)
    
    while nao_visitados:
        transporte_atual = None
        atual = min(nao_visitados, key=lambda v: dist[v])
        nao_visitados.remove(atual)
        
        for vizinho, transporte in grafo[atual].items():
            if transporte == transporte_atual:
                dist[vizinho] = min(dist[vizinho], dist[atual])
            else:
                if dist[vizinho] + transportes[transporte-1][1] > dist[atual] + transportes[transporte-1][1]:
                    dist[vizinho] = dist[atual] + transportes[transporte-1][1]
                    transporte_atual = transporte
    return dist

ans = dijkstra(grafo, a)[b]
print(ans if ans != float('inf') else -1)