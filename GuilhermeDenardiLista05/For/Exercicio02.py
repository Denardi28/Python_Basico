#Exercicio 02

R1 = 0
Cont = int(input("Quantos números positivos você quer tirar a média "))
x = 1
for i in range(0, Cont):
    resp = int(input("Digite o %d número: " % x))
    R1 = R1 + resp
    x = x + 1
R2 = R1 / Cont
print("A média dos valores é", R2)
