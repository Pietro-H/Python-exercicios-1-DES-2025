#Crie um programa que calcule o reajuste de salário:

#Salários até R$ 2000,00: +15%
#De R$ 2000,01 a R$ 5000,00: +10%
#Acima de R$ 5000,00: +5%

salario = float(input("Digite Seu salário:"))

reajuste01 = salario *0.15
reajuste02 = salario *0.10
reajuste03 = salario *0.5

if salario <= 2000:
    print("Você ganhou um reajuste de mais 15%, que foi de +" , reajuste01)
elif salario <= 5000 :
    print("Você ganhou um reajuste de mais 10% que foi de +" , reajuste02)
elif salario  >= 5001:
    print("Você ganhou um reajuste de mais 5% que foi de +" , reajuste03)

