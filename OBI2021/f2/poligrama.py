n = int(input())
poligrama = input()

p1, p2 = poligrama[:n//2], poligrama[n//2:]

while len(p1) != len(p2):
    p1, p2 = p2[:len(p2)//2], p2[len(p2)//2:]
quebra = False
for letra in range(len(p1)):
    if p1[letra] not in p2:
        print("*")
        quebra = True
        break
    else:
        index = p2.index(p1[letra])
        try:
            p2 = p2[:index] + p2[index+1:]
        except:
            p2 = p2[:index]

if quebra == False:
    print(p1)