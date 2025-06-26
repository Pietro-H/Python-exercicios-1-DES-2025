# Isabela está desenvolvendo um aplicativo de corrida que calcula a velocidade média do usuário.
# O programa deve receber a distância percorrida e o tempo gasto, calcular a velocidade e indicar se foi 
# lenta (<5 km/h), moderada (5 a 10 km/h) ou rápida (>10 km/h).

distancia = float(input("Digite sua distancia percorrida: "))
tempo = float(input("Digite seu tempo gasto: "))

V_media = distancia / tempo 
print(f"{V_media:.2f} km/h")

if V_media < 5:
    print("Velocidade lenta.")
elif V_media < 10:
    print("Velocidade modereda.")
else:
    print("velocidade rapida")





