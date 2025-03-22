n, q = [int(v) for v in input().split()]
lista = input().split()
for _ in range(q):
    indices = [int(v) for v in input().split()]
    intervalo = lista[indices[0]-1:indices[1]]
    n = indices[1]-indices[0]+1
    print(sum([int(intervalo[i]+intervalo[j]) for i in range(n) for j in range(n) if i != j]))