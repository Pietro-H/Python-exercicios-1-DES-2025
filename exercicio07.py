# Uma empresa quer avaliar seus colaboradores com base em três metas atingidas.
# O programa deve calcular a média das três avaliações e exibir:

# Aprovado (>=7)
# Em treinamento (>=5 e <7)
# Reprovado (<5)

media1 = float(input("Digite sua primeiro média:"))
media2 = float(input("Digite sua sugunda média:"))
media3 = float(input("Digite sua terceira média:"))

soma = media1 + media2 + media3/3

if soma >= 7:
    print("Apravoda.")
elif soma >= 5 <7:
    print("Em treinamento.")
elif soma <5:
    print("reprovado.")

