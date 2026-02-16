#Exercicio 4
import os 


#Entrada
Sal = float(input("Qual o valor do salário atual? "))
Am = float(input("Qual a porcentagem do aumento? "))




#Processamento
SalN = Sal  * (Am/100)
Resp1 = Sal + SalN




#Saida
print("O novo salário é", Resp1, "reais e o aumento foi de", SalN, "reais")
os.system('pause')
