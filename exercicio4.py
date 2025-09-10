#4. Leia a nota final de três provas (0 a 10). Calcule a média e informe:
#a. Média ≥ 7: aprovado
#b. Média ≥ 5 e <7: recuperação
#c. Média <5: reprovado
#d. Se alguma nota for 0: reprovado automático


media1 = float(input("Digite a nota 1: "))
media2 = float(input("Digite a nota 2: "))
media3 = float(input("Digite a nota 3: "))

media = (media1 + media2 + media3) / 3

if media >= 7:
  print("Aprovado")
elif media >= 5 and media < 7:
  print("Recuperação")
elif media < 5:
  print("Reprovado")
elif media == 0:
  print("Reprovado automático")
else:
  print("erro")