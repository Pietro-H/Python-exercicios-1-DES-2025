#Crie um programa que receba o peso (kg) e a altura (m) de uma pessoa e calcule o IMC.
#Classifique o resultado de acordo com a faixa:

#Abaixo do peso (< 18.5)
#Peso normal (18.5 a 24.9)
#Sobrepeso (25 a 29.9)
#Obesidade (>= 30)

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso/altura**2

if imc <18.5:
    print("Abaixo do peso:" , imc)
elif 18.5 <= imc <= 24.5:
    print("Peso normal:" , imc)
elif 25 <= imc <= 29.9:
    print("sobrepeso:" , imc)
elif imc >= 30:
    print("obesidade:" , imc)


