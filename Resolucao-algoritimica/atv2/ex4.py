"""
4. Peça usuário e senha.

Só permita acesso se usuário for "admin" e a senha for "1234".
Caso contrário, bloqueie.
Se o usuário for "convidado" e não digitar senha, exiba “Acesso restrito”.
"""

user = input("Digite o usuário: ")
password = input("DIgite a senha: ")

if user == "convidado" and password == "":
    print("Acesso restrito")

elif user == 'admin' and password == "1234":
    print(f"Acesso permitido, seja bem vindo {user}!")

else:
    print("Acesso bloqueado, usuário e senha inválidos.")