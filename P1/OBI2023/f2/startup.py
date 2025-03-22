n = int(input())
id = 0
insatisfeitos = 0
funcionarios = []
def print_insatisfeitos(funcionarios):
    for funcionario in funcionarios:
        if any(subordinado['salario'] > funcionario['salario'] for subordinado in funcionario['subordinados']):
            funcionario['satisfeito'] = False
        elif funcionario['satisfeito'] == False:
            funcionario['satisfeito'] = True
    print(sum(1 for funcionario in funcionarios if not funcionario['satisfeito']))
for i in range(n):
    chefe, salario = list(map(int, input().split()))
    id += 1
    funcionario = { 'id' : id,
                    'chefe' : chefe,
                    'salario' : salario,
                    'satisfeito' : True,
                    'subordinados' : []}
    funcionarios.append(funcionario)
    funcionarios[chefe-1]['subordinados'].append(funcionario)

print_insatisfeitos(funcionarios)

n = int(input())
for i in range(n):
    funcionario, salario = list(map(int, input().split()))
    funcionarios[funcionario-1]['salario'] = salario
    print_insatisfeitos(funcionarios)