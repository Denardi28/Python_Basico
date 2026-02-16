#Exercício 02

estoque = {
"mouse": 50,
"teclado": 30,
"monitor": 15,
"fone": 20
}

Produto = input("Digte um produto: ")
# Verificando se chave existe
if Produto in estoque:
    print(f"Como o produto desejado existe: {estoque[Produto]}")
else:
    print("Produto não existe")
