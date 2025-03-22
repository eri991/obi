n = int(input())
senhas = []
for i in range(n):
    senhas.append(input())

count = 0
for j in range(n-1):
    for i in range(n-1):
        if senhas[i] in senhas[j+1]:
            count += 1

print(count)