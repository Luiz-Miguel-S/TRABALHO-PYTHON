#7. Receba idade, renda mensal e dívidas. Classifique risco:
#a. Alta: renda < 2000 e dívidas > 50% da renda
#b. Média: renda 2000–5000 ou dívidas 30–50%
#c. Baixa: renda > 5000 e dívidas < 30%
#d. Outros casos: médio-baixo



# Receber dados do usuário
idade = int(input("Digite sua idade: "))
renda = float(input("Digite sua renda mensal: "))
dividas = float(input("Digite o valor total das dívidas: "))

# Calcular percentual da dívida em relação à renda
if renda > 0:
    perc_divida = (dividas / renda) * 100
else:
    perc_divida = 0  # evita divisão por zero
    print("Atenção: renda igual a zero!")

# Classificação do risco
if renda < 2000 and perc_divida > 50:
    risco = "Alto"
elif (2000 <= renda <= 5000) or (30 <= perc_divida <= 50):
    risco = "Médio"
elif renda > 5000 and perc_divida < 30:
    risco = "Baixo"
else:
    risco = "Médio-Baixo"

# Exibir resultado
print(f"\nClassificação de risco: {risco}")