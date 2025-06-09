import random

frutas = ["maça", "Banana", "Laranja", "Uva", "manga"]

print("Lista de Frutas:")
for i in range(len(frutas)):
    print(f"{i + 1} - {frutas[i]}")

posicao_sorteada = random.randint(1,5)

palpite = input("Qual fruta você acha que está na posição sorteada?")

fruta_certa = frutas[posicao_sorteada - 1]
 
if palpite.capitalize() == fruta_certa:
   print("parabéns! Você acertou!")
   print(f"A fruta na posição {posicao_sorteada} era realmente {fruta_certa}.")
else:
    print("Que pena, você errou.")
    print(f"A fruta na posição {posicao_sorteada} era {fruta_certa}.")