#Exercicio 8
import os 


#Entrada
QKM = float(input("Qual a distância percorrida? "))
QDI = int(input("Qual a quantidade de dias que foi alugado? "))



#Processamento
R1 = QKM * 0.15
R2 = QDI * 60
R3 = R2 + R1



#Saida
print("Você deve pagar", R3, "Reais")
os.system('pause')
