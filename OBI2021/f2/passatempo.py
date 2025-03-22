l, c = list(map(int, input().split()))
matriz = []
somas_linhas = []
colunas = []
vars = {}
for _ in range(l):
    inpu = input().split()
    matriz.append(inpu[:c])
    somas_linhas.append(int(inpu[-1]))
    for var in inpu[:c]:
        vars[var] = None
somas_colunas = list(map(int, input().split()))

for i in range(c):
    coluna = []
    for j in range(l):
        coluna.append(matriz[j][i])
    colunas.append(coluna)
achadas = 0
num_vars = len(vars)
for _ in range(num_vars):
    for col in range(c):
        coluna = colunas[col]
        if len(set(coluna)) == achadas+1:
            vars[coluna[0]] = somas_colunas/l
            achadas += 1
        

for var, val in vars.items():
    print(var, val)