# Isabela está desenvolvendo um aplicativo de corrida que calcula a velocidade média do usuário.
# O programa deve receber a distância percorrida e o tempo gasto, calcular a velocidade e indicar se foi 
# lenta (<5 km/h), moderada (5 a 10 km/h) ou rápida (>10 km/h).

tempo = int(input("Digite seu tempo gasto:"))
distancia = int(input("Digite sua distancia percorrida:"))

velocidadeM = distancia / tempo
print(f"{velocidadeM:.2f} km/h")

if velocidadeM < 5:
    print("Velocidade lenta.")
elif velocidadeM < 10:
    print("Velocidade modereda.")
elif velocidadeM > 10:
    print("velocidade rapida")





