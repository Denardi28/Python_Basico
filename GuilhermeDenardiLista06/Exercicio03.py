'''
3: Acesso a Listas Aninhadas
Dada a lista dados = ["Python", [10, 20, 30], "Academy"] , faça:
1. Acesse e imprima o segundo elemento da lista interna [10, 20, 30] .
2. Substitua "Academy" por "Programming" na lista principal.
3. Imprima a lista final.
'''


dados = ["Python", [10, 20, 30], "Academy"]
print(dados[1][1])
dados[2] = "programming"
print(dados)
