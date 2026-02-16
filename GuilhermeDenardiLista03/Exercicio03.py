#Exercicio 3
import os 

#Entrada
dia = int(input("Quantos dias? "))
Ho = int(input("Quantas Horas? "))
Min = int(input("Quantos minutos? "))
seg = int(input("Quantos segundos? "))





#Processamento
C1 = dia * 24
C2 = (C1 + Ho)* 60
C3 = (C2 + Min) * 60
C4 = C3 + seg




#Saida
print("O total em segundos é", C4)
os.system('pause')
