#Peça a idade do usuário e diga se ele pode se cadastrar em um site:

#Permitido: 13 anos ou mais

idade = int(input("Digite a sua idade:"))


if idade >= 13:
    print("Você está permetido entrar.")
elif idade < 13:
    print("Você não tem idade permitida.")



