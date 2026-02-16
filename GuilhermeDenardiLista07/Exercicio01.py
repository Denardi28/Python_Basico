#Exercício 01

alunos = {}
Nome01 = input("Qual o seu nome? ")
Idade01 = input("Qual a sua idade? ")
Nota01 = input("Qual a sua nota? ")
alunos.update({'Nome': Nome01})
alunos.update({'Idade':Idade01})
alunos.update({'Nota': Nota01})
for chave in alunos.keys():
    print(f" Indice = {chave} e Valor = {alunos[chave]}")


