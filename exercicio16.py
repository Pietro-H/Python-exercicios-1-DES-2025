#Crie um programa que calcule o reajuste de salário:

#Salários até R$ 2000,00: +15%
#De R$ 2000,01 a R$ 5000,00: +10%
#Acima de R$ 5000,00: +5%

salario = float(input("Digite Seu salário:"))
porcentagem = float(input("Digite sua porcentagem:"))

calcule01 = salario /0.15
calcule02 = salario /0.10
calcule03 = salario /0.5

if salario