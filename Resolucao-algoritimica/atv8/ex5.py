"""
5. Implemente uma calculadora simples em Python utilizando funções. A
calculadora deve ser capaz de realizar as seguintes operações
matemáticas básicas:
• Soma
• Subtração
• Multiplicação
• Divisão
Requisitos:
• Crie uma função para cada operação matemática (soma,
subtração, multiplicação e divisão). As funções devem receber
dois valores e retornar o resultado da operação.
• Implemente uma função para exibir o menu de opções para o
usuário.
• O programa deve repetir o menu após cada operação, até que
o usuário escolha a opção de sair.
"""

def soma(a,b):
    return a + b

def subtracao(a,b):
    return a - b

def multiplicacao(a,b):
    return a*b

def divisao(a,b):
    return a/b

def menu():
    print("\n======== CALCULADORA ========")
    print("0. Sair")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    opcao = input(str("\nQual operação deseja realizar?: "))

    while(opcao != "1" and 
          opcao != "2" and
          opcao != "3" and
          opcao != "4" and
          opcao != "0"):
        opcao = input(str("\nQual operação deseja realizar?: "))

    opcao = int(opcao)

    if(opcao == 0):
        return False
    
    a = int(input("número: "))
    b = int(input("número: "))

    if(opcao == 1):
        print(soma(a,b))

    elif(opcao == 2):
        print(subtracao(a,b))

    elif(opcao == 3):
        print(multiplicacao(a,b))

    elif(opcao == 4):
        print(divisao(a,b))


while True:
    if(not menu()):
        print("tchauzinho")
        break
    
