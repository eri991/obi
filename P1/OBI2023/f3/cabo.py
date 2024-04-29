numeros = list(map(int, input().split()))
quebra = False
for x in numeros:
    for y in numeros:
        for z in numeros:
            if x+y+z == sum(numeros)-x-y-z:
                print("S")
                quebra = True
                break
        if quebra:
            break
    if quebra:
        break
if quebra == False:
    print("N")