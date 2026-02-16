Idade = int(input("Qual sua idade? "))

if Idade >= 16 and Idade < 18 or Idade >= 70:
    print("Pode votar mas não é obrigatório")
elif Idade < 16:
    print("Não pode votar")
elif Idade >= 18 and Idade < 70:
    print("Voto obrigatório")
