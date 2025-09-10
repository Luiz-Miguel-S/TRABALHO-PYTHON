# Peça o salário do funcionário e o tempo de empresa.
# Calcule o bônus considerando as seguintes regras: a. Salário < 2000 e tempo ≥ 5 anos: bônus de 20% 
# b. Salário < 2000 e tempo < 5 anos: bônus de 10% c. Salário ≥ 2000 e tempo ≥ 5 anos: bônus de 5% 
# d. Salário ≥ 2000 e tempo < 5 anos: sem bônus


salario = int(input("Digite seu salario: "))
tempo = int(input("Digite seu tempo de empresa"))

if salario < 2000 and tempo >= 5:
  print(salario + (salario * 0.20))
elif salario < 2000 and tempo < 5:
  print(salario + (salario * 0.10))
elif salario >= 2000 and tempo >= 5:
  print(salario + (salario * 0.05))
elif salario >= 2000 and tempo < 5:
  print(salario and ("sem bonus entregue"))
else:
  print("erro")