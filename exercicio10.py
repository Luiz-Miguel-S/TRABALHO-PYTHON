#10. O sistema solicita uma senha ao usuário, informando as regras, e exibe senha
#válida se as seguintes regras forem atendidas:
#a. Mínimo 8 caracteres
#b. Contém pelo menos 1 maiúscula, 1 minúscula, 1 número e 1 dos seguintes
#símbolos: !@#$%


import string

Passworld = input("Digite a sua senha: ")

qtde_mai = 0
qtde_min = 0
qtde_num = 0
qtde_simb = 0

for caractere in Passworld:
    if caractere.isupper(): #verifica se é maiúscula
        qtde_mai += 1
    elif caractere.islower(): #verifica se é minúscula
        qtde_min += 1
    elif caractere.isdigit(): #verifica se é número
        qtde_num += 1
    elif caractere in string.punctuation: #verifica se é símbolo especial
        qtde_simb += 1

#valida as regras
#O len verifica quantos caracteres a senha tem
if (len(Passworld) >= 8 and 
    qtde_mai >= 1 and
    qtde_min >= 1 and 
    qtde_num >= 1 and
    qtde_simb >= 1):
    print("Senha válida!")

else:
    print("Senha inválida!")
    print("A senha deve conter pelo menos:")
    if len(Passworld) < 8:
        print("- 8 caracteres")
    if qtde_mai < 1:
        print("- 1 letra maiúscula")
    if qtde_min < 1:
        print("- 1 letra minúscula")
    if qtde_num < 1:
        print("- 1 número")
    if qtde_simb < 1:
        print("- 1 símbolo especial")
        