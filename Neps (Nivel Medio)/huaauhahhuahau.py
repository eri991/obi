vogais, vogaisRisada = "aeiou", ""
for i in input():
    vogaisRisada += i if i in vogais else ""
print("S") if vogaisRisada == vogaisRisada[::-1] else print("N")