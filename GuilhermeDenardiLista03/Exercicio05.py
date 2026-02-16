#Exercicio 5
import os 


#Entrada
Sal = float(input("Qual o valor ds mercadoria? "))
Am = float(input("Qual a porcentagem do desconto? "))




#Processamento
SalN = Sal  * (Am/100)
Resp1 = Sal - SalN




#Saida
print("O novo preço é", Resp1, "reais e o desconto foi de", SalN, "reais")
os.system('pause')
