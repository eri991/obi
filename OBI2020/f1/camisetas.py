n = int(input())
lista = list(map(int, input().split()))
pequenosProduzidos, mediosProduzidos = int(input()), int(input())
print("N") if lista.count(1) < pequenosProduzidos or lista.count(2) < mediosProduzidos else print("S")