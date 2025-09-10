#6. Peça idade e nacionalidade. Informe se pode votar:
#a. Apenas maiores de 18
#b. Brasileiros: obrigatório, estrangeiros: opcional
#c. Entre 16 e 17 anos: opcional

idade = int(input("Digite sua idade: "))
nacionalidade = input("Digite sua nacionalidade: Brasileiro ou Estrangeiro ")

if idade >= 18 and nacionalidade == "Brasileiro":
  print("Obrigatorio votar")
elif idade >= 16 and idade <= 17 and nacionalidade == "Brasileiro":
  print("Opcional votar")
elif idade >= 18 and nacionalidade == "Estrangeiro":
  print("Opcional votar")
else:
  print("Não pode votar")