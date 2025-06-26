#Peça ao usuário uma senha e verifique se ela contém pelo menos 8 caracteres.
#Exiba uma mensagem de "Senha válida" ou "Senha muito curta".

senha = input("digite uma senha: ")

caracteres = len(senha)
if caracteres >=8:
    print("senha válida.")
elif caracteres <=8:
    print("senha muito curta.")