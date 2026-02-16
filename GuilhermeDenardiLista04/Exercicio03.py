#Exercicio 03
import os

#Entrada
N1 = float(input("Digite o primeiro número: "))
#N1 = Número 1
N2 = float(input("Digite o segundo número: "))
#N2 = Número 2
R1 = str(input("Qual a operação? "))
#R1 = A operação que você vai fazer



#Processamento

if R1 == "/":
   R =  N1 / N2
elif R1 == "+":
    R= N1 + N2
elif R1 == "*":
    R= N1 * N2
elif R1 == "-":
    R= N1 - N2

#Saida
print("O resultado é", R)
#R = Resposta
os.system("pause")



