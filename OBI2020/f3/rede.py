n = int(input())
repostagens = []
for i in range(n):
    repostagens.append(int(input()))
repostagens.sort()
inicio = 0
fim = n
while fim-inicio > 1:
    count = 0
    meio = (fim+inicio)//2
    
    