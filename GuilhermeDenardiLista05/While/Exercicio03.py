#Exercicio 03

s = 0
x = 0
while True:
    v = int(input("Digite um número positivo ou negativo para sair: "))
    if v < 0:
        break
    if v % 2 == 0:
        print("É par")
    else:
        print("É ímpar")
        x = x + 1
print("Tem", x, "números pares")
 
