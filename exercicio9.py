#9. O usuário digita um preço de um produto e se ele é um cliente vip ou não e o
#sistema exibe o preço do produto com desconto baseado nas seguintes regras:
#a. Produto ≥ 100: desconto 20%
#b. Produto ≥ 50 e <100: desconto 10%
#c. Produto <50: sem desconto
#d. Cliente VIP: +5% desconto adicional

preco = float(input("Digite o preço do produto: R$ "))
vip = input("O cliente é VIP? (sim/não): ").lower()

desconto = 0

if preco >= 100:
    desconto = 0.20
elif preco >= 50:
    desconto = 0.10
else:
    desconto = 0.00

if vip == "ssim":
    desconto += 0.05

preco_final = preco * (1 - desconto)

print(f"\nPreço original: R$ {preco:.2f}")
print(f"Desconto aplicado: {desconto*100:.0f}%")
print(f"Preço final: R$ {preco_final:.2f}")