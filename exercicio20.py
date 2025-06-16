#Simule um login com nome de usuário "admin" e senha "1234".
#Caso os dados estejam corretos, exiba "Acesso concedido", senão "Acesso negado".

nome_correto = "admim"
senha_correta = "1234"

login = input("Digite seu nome de usuario: ")
senha = input("digite sua senha: ")

if login == nome_correto and senha == senha_correta:
    print("acesso concedido")
else:
    print("acesso negado")





