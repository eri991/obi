n = int(input())
lista = list(map(int, input().split()))
duplas = 0

for i in range(n):
    for j in range(n):
        if lista[i] > lista[j] and i < j:
            duplas += 1

print(duplas)