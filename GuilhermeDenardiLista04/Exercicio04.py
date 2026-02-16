#Exercicio 04
import os

#Entrada
Cs = float(input("Qual o valor da casa? "))
#Cs = Valor da casa
Sal = float(input("Qual seu salário? "))
#Sal = Salário
An = float(input("Você vai pagar em quantos anos? "))
#An = Anos que vai pagar



#Processamento
Mn = 12 * An
#Mn = Meses de prestação
Pr = Cs / Mn
#Pr = Valor da prestação
Sal30 = Sal * 0.3
#Sal30 = 30% do salário
if Pr > Sal30:
    print("Não podemos fazer o empréstimo")
else:
    print ("Você pode fazer o empréstimo")
print("A prestação foi de", Pr, "reais")

os.system("pause")
