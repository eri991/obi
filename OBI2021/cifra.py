palavra = input()
vogais = "aeiou"
consoantes = "bcdfghjklmnpqrstvwxyz"
alfabeto = "abcdefghijklmnopqrstuvwxyz"
indexes = []

for i in alfabeto:
    if i in vogais:
        indexes.append(alfabeto.index(i))

novaPalavra = ''
for i in palavra:
    novaPalavra += i
    if i in consoantes:
        maisProxima = "a"
        for x in indexes:
            if abs(x-alfabeto.index(i)) < abs(alfabeto.index(maisProxima)-alfabeto.index(i)):
                maisProxima = alfabeto[x]
        novaPalavra += maisProxima
        novaPalavra += consoantes[consoantes.index(i)+1] if i != "z" else "z"

print(novaPalavra)