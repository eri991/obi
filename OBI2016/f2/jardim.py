pontos = [tuple(int(v) for v in input().split()) for _ in range(7)]
x = [tupla[0] for tupla in pontos]
y = [tupla[1] for tupla in pontos]
colineares = [y.count(x) for x in y]
print(f"{pontos} \n{x}\n{y}\n{colineares}")
