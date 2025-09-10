#5. Peça dia, mês e ano. Verifique se a data é válida (meses com 30 ou 31 dias,
#fevereiro com 28/29).

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

if mes < 1 or mes > 12 or dia < 1:
    print("Data invalida")
elif mes == 2 and dia > 29:
    print("Data invalida")
elif (mes in [4, 6, 9, 11]) and dia > 30:
    print("Data invalida")
elif (mes in [1, 3, 5, 7, 8, 10, 12]) and dia > 31:
    print("Data invalida")
else:
    print("Data valida")
