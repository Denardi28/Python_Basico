#Exercicio 9
import os 


#Entrada
CDI = int(input("Qual a quantidade de cigarros fumados por dia? "))
CDA = int(input("Por quantos anos você fumou? "))



#Processamento
R1 = 365 * CDA
R2 = CDI * R1
R3 = R2 * 10
R4 = R3 / 24




#Saida
print("Você perdeu", R4, "dias de vida")
os.system('pause')
