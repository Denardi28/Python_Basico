#Exercicio 01

F1 = 0
M1 = 0
for i in range(0, 10):
    resp = str(input("É de qual sexo? "))
    if resp == "m" or resp == "M":
        M1 = M1 + 1
    if resp == "f" or resp == "F":
        F1 = F1 + 1
print("Tem", M1, "pessoas do sexo masculino e", F1, "pessoas do sexo feminino")
