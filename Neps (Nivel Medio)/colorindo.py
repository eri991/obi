n, m, x, y, k = list(map(int, input().split()))
grade = [[0]*(m+1)]*(n+1)
for i in range(k):
    a, b = list(map(int, input().split()))
    grade[a][b] = 1

def bfs(grade):
    fila = [(x, y)]
    quadrados = 0
    verificados = []
    while len(fila) >= 1:
        quadrados += 1
        a, b = fila.pop()
        verificados.append((a, b))
        if a < n and grade[a+1][b] != 1 and (a+1, b) not in verificados:
            fila += [(a+1, b)]
            if b < m and grade[a+1][b+1] != 1 and (a+1, b+1) not in verificados:
                fila += [(a+1, b+1)]
            if b > 1 and grade[a+1][b-1] != 1 and (a+1, b-1) not in verificados:
                fila += [(a+1, b-1)]
        if a > 1 and grade[a-1][b] != 1 and (a-1, b) not in verificados:
            fila += [(a-1, b)]
        if b < m and grade[a][b+1] != 1 and (a, b+1) not in verificados:
            fila += [(a, b+1)]
            if a < n and grade[a+1][b+1] != 1 and (a+1, b+1) not in verificados:
                fila += [(a+1, b+1)]
            if a > 1 and grade[a-1][b+1] != 1 and (a-1, b+1) not in verificados:
                fila += [(a-1, b+1)]
        if b > 1 and grade[a][b-1] != 1 and (a, b-1) not in verificados:
            fila += [(a, b-1)]
    return quadrados

print(bfs(grade))
        