'''
9: Análise de Lista
Dada a lista notas = [7.5, 8.0, 6.5, 9.0, 8.0, 7.5] :
1. Conte quantas vezes a nota 8.0 aparece.
2. Encontre a posição da primeira ocorrência de 7.5.
3. Identifique a menor e a maior nota da lista.
'''

notas = [7.5, 8.0, 6.5, 9.0, 8.0, 7.5]
nota01 = notas.count(8)
print("A nota 8 aparece", nota01, "vezes")
nota02 = notas.index(7.5)
print("O número 7.5 aparece pela primeira vez na posição", nota02)
print("O menor valor das notas é:", min(notas))
print("O maior valor das notas é:", max(notas)) 

