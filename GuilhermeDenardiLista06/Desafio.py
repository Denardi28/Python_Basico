lista_compras = []
while True:
    print("\n--- LISTA DE COMPRAS ---")
    print("1. Adicionar item")
    print("2. Ver lista")
    print("3. Remover um item")
    print("4. Quantidade de itens")
    print("5. Sair")
    opcao = input("Escolha a opção desejada:")
    if opcao == "1":
        lista_compras.append(input("Qual produto: "))
        lista_compras.sort()
        print("Seu produto foi adicionado")
    if opcao == "2":
        print("Os produtos da sua lista são", lista_compras)
    if opcao == "3":
        excluir = int(input("Em qual posição o produto que você quer excluir está? "))
        lixo = lista_compras.pop(excluir)
    if opcao == "4":
        print(len(lista_compras))
    if opcao == "5":
        break
    if opcao != "1" and opcao != "2" and opcao != "3" and opcao != "4" and opcao != "5":
        print("Opcão não disponível")
