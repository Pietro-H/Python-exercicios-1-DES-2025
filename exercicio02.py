#  Juliana está coordenando entregas de projetos e precisa calcular o tempo total necessário 
# para finalizar três tarefas: X, Y e Z.
#  Se alguma tarefa estiver com o tempo de entrega negativo, deve-se exibir uma mensagem de 
# erro e não somar o total.
#Soma OK, negativo não funciona

tarefa_1 = int(input("Dias para tarefa_1:"))
tarefa_2 = int(input("Dias para tarefa_2:"))
tarefa_3 = int(input("Dias para tarefa_3:"))

if tarefa_1 < 0 or tarefa_2 < 0 or tarefa_3 < 0 :
    print("ERRO!! numeros negativo")
else:
    soma = tarefa_1 + tarefa_2 + tarefa_3
    print(f"Tempo total do projeto: {soma} dias")