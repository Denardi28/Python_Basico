#Exercicio 01
import os

#Entrada
Vm = int(input("Qual a velocidade do carro: "))
#Vm = velocidade média



#Processamento e saida
Rf = 5 * (Vm - 80)
#Rf = Resultado final
if Vm > 80:
    print("Você foi multado em: R$", Rf)
else:
    print("Você não foi multado")
os.system("pause")




