n = int(input())
lista = []
maior = 0
for i in range(n):
    lista.append(int(input()))
if n == 1:
    print(1)
else:
    for a in range(n):
        for b in lista[a:]:
            if b == lista[a]:
                continue
            count = 0
            foco = lista[a]
            for c in lista:
                if c == foco:
                    count += 1
                    foco = lista[a] if foco == b else b
            maior = max(maior, count)
    maior = 1 if maior == 0 else maior
    print(maior)