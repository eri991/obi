divertido = 0
chateado = 0
frase = input()

for index in range(len(frase)):
    if frase[index] == ":" and index < len(frase)-2:
        # Identifica se são os olhos da carinha e se o index não estrapola o tamanho da string (prevenindo um erro)
        if frase[index+1] == "-":
            # Caso o próximo caractere seja o nariz,
            if frase[index+2] == ")":
                # checa se é um sorriso, caso sim, adiciona ponto divertido
                divertido += 1
            elif frase[index+2] == "(":
                # caso não, se for boca triste, adiciona ponto chateado
                chateado += 1

if divertido == chateado:
    print("neutro")
elif divertido > chateado:
    print("divertido")
else:
    print("chateado")