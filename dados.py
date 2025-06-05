import random

input("Pressione o enter para lançar o dado:")


resultado = random.randint(1,6)


print (f" 0 dado rolou : {resultado}" );

if resultado >=6:
    print("UAU!! você é fera.")
elif resultado >2 <6:
    print("Vamos la você está quase.")
elif resultado <2:
    print("Não foi dessa vez, tente novamente.")






























