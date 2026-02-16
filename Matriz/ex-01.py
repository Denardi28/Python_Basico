matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

totalizador = 0

for linha in matriz:
    print("Linha: ",linha)
    for valor in linha:
        totalizador += valor
print("Total: ",totalizador)       

