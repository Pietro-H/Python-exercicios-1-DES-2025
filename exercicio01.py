# Gabriel está acompanhando o desempenho de dois cursos online que lançou: Python Básico e JavaScript Essencial.
# Ele quer saber qual curso teve mais avaliações no último mês.

# Crie um programa que receba o número de avaliações de cada curso e exiba qual teve mais.
# Caso as quantidades sejam iguais, exiba uma mensagem dizendo que houve empate.

curso01 = int(input("digite quantas avaliações o curso01 teve: "))
curso02 = int(input("digite quantas avaliações o curso02 teve: "))


if curso01 > curso02:
    print("curso01 teve mais avaliações")
elif curso02 > curso01:
    print("curso02 teve mais avaliações")
else:
    print("os dois cursos tiveram as mesmas avaliações")