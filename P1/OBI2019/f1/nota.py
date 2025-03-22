"""
Trapezio esquerda - Felix 
Trapezio direita - Marzia
Trapezio total - 70*160 = 11200
Caso esquerda = direita, print(0)

input duas linhas com cada base do trapezio

print(1) se esquerda > direita
print(2) se for o contrario
senao print(0)
"""

b, t = int(input()), int(input())
area_total = 11200
area_esquerda = ((b+t)*70)/2
area_direita = area_total-area_esquerda

if area_esquerda > area_direita:
    print(1)
elif area_direita > area_esquerda:
    print(2)
else:
    print(0)