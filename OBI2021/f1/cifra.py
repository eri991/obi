palavra = input()
vogais = "aeiou"
consoantes = "bcdfghjklmnpqrstvwxz"
alfabeto = "abcdefghijklmnopqrstuvwxyz"
vogaisIndexes = [0,4,8,14,20]
novaPalavra = ''
for i in palavra:
    novaPalavra += i
    if i in consoantes:
        maisProxima = "a"
        for x in vogaisIndexes:
            if abs(x-alfabeto.index(i)) < abs(alfabeto.index(maisProxima)-alfabeto.index(i)):
                maisProxima = alfabeto[x]
        novaPalavra += maisProxima
        novaPalavra += consoantes[consoantes.index(i)+1] if i != "z" else "z"

print(novaPalavra)