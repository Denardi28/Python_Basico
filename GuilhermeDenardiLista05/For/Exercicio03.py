#Exercicio 03

R1 = 0
x = 1
for i in range(0, 100):
    resp = int(input("Digite o %d número: " % x))
    if resp >= 100 and resp <= 200:
        R1 = R1 + 1
    if resp == 0:
        break
    x = x + 1
print("Tem", R1, "números entre 100 e 200")
