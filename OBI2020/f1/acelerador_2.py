d = int(input())
resto = (d-3)%8
# Diminuimos 3 de "d" porque é a distância até o início da trajetória
# A medida do circulo do acelerador é 8.
# Partindo do primeiro ponto e atravessando 8 unidades, paramos no mesmo local
# Sendo assim, o que importa é o resto de uma divisão por 8
if resto == 3:
    print(1)
elif resto == 4:
    print(2)
elif resto == 5:
    print(3)