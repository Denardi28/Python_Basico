'''
10: Manipulação Avançada
Dadas as listas:
frutas = ["Maçã", "Banana"]
hortifruti = ["Cenoura", "Abacaxi"]
1. Combine frutas e hortifruti em uma única lista.
2. Remova o último item da lista resultante e armazene-o em uma variável.
3. Ordene a lista final em ordem alfabética.
4. Imprima a lista ordenada e o item removido.
'''
frutas = ["Maçã", "Banana"]
hortifruti = ["Cenoura", "Abacaxi"]
frutas.extend(hortifruti)
lista_copiada = frutas.pop(3)
frutas.sort()
print("Essa é a lista", frutas, "e o item removido é", lista_copiada)



