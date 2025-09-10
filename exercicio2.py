# 2. Receba três lados e informe se formam um triângulo. Classifique como: 
# equilátero, isósceles ou escaleno. 


lado1 = int(input("Digite o lado 1: "))
lado2 = int(input("Digite o lado 2: "))
lado3 = int(input("Digite o lado 3: "))

if lado1 == lado2 == lado3:
  print("equilátero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
  print("isósceles")
else:
  print("escaleno")
