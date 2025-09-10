#8. Dado a sequência 'B', 'C', 'D', 'A' para as 4 cartas (A, B, C, D), o usuário escolhe a
#sequência de 4 cartas e recebe uma pontuação baseada nas seguintes regras:
#a. Resposta correta: 10 pontos para cada acerto
#b. Resposta A: bônus 5 pontos independente de estar certo
#c. Resposta C seguida de D na sequência: bônus extra 5 pontos independente
#de estar certo
#d. Sistema exibe a pontuação do usuário.
#Obs: Pontuação máxima = 50.

gabarito = ['B', 'C', 'D', 'A']

print("Escolha a sequência de 4 cartas (A, B, C ou D).")
resposta = []
for i in range(4):
    carta = input(f"Digite a {i+1}ª carta: ").upper()
    while carta not in ['A', 'B', 'C', 'D']:
        carta = input("Entrada inválida. Digite A, B, C ou D: ").upper()
    resposta.append(carta)

pontos = 0

for i in range(4):
    if resposta[i] == gabarito[i]:
        pontos += 10

pontos += resposta.count('A') * 5

for i in range(3):
    if resposta[i] == 'C' and resposta[i+1] == 'D':
        pontos += 5
        break  

if pontos > 50:
    pontos = 50

print(f"\nSua sequência: {resposta}")
print(f"Pontuação final: {pontos}")
