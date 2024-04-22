n = int(input())
m = int(input())
"""
'a diferença de idade dos dois irmãos mais novos'
    m - n
'é igual a diferença de idade dos dois irmãos mais velhos'
    m - n = resultado - m
Assim desenvolvemos a equação, somando m dos dois lados (pois não altera o resultado)
    m - n + m = resultado - m + m
    2*m-n = resultado
"""
print(2*m-n)