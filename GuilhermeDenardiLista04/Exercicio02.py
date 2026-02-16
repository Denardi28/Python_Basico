#Exercicio 02
import os

#Entrada
Sal = float(input("Qual o salário do funcionário? "))
#Sal = salário

#Processamento e saida
R1 = Sal * (10/100) + Sal
#R1 = Salário se for maior que 1250
R2 = Sal * (15/100) + Sal
#R2 = Salário se for menor que 1250
if Sal > 1250:
    print("Seu novo salário é de R$", R1)
else:
    print("Seu novo salário é de R$", R2)
os.system("pause")   
