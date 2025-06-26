# Rafael trabalha com armazenamento de grãos e precisa garantir que a umidade do ar no local não ultrapasse 70%.
# Escreva um programa que receba o valor da umidade atual e exiba um alerta se estiver acima do limite.

unidade = int(input("Digite a unidade local: "))

if unidade >= 70:
    print("Alerta unidade ultrapassa 70%")
else:
    print("Unidade dentro do padrão")