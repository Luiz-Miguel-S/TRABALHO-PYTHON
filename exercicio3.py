#3. Leia peso e altura, calcule o IMC e classifique:
#a. <18.5: abaixo do peso
#b. 18.5–24.9: peso normal
#c. 25–29.9: sobrepeso
#d. 30–34.9: obesidade grau I
#e. 35–39.9: obesidade grau II
#f. ≥40: obesidade grau III


peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura * altura)

if imc < 18.5:
  print("Abaixo do peso")
elif imc >= 18.5 and imc <= 24.9:
  print("Peso normal")
elif imc >= 25 and imc <= 29.9:
  print("Sobrepeso")
elif imc >= 30 and imc <= 34.9:
  print("Obesidade grau I")
elif imc >= 35 and imc <= 39.9:
  print("Obesidade grau II")
else:
  print("Obesidade grau III")