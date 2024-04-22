n = int(input())
lista = input().split()
pequenosProduzidos = int(input())
mediosProduzidos = int(input())
if lista.count("1") < pequenosProduzidos or lista.count("2") < mediosProduzidos:
    print("N")
    # Se a quantidade de pequenos na lista é menor que a produzida
    # ou se a quantidade de médios na lista é menor que a produzida
    # o resultado é "N", pois não tem camisas suficientes
else:
    print("S")
    # Caso contrário, tem o suficiente, resultando "S"