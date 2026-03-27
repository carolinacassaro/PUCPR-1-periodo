"""
6. Desenvolvimento de uma calculadora em Python com menu de opções

Implemente um programa em Python que funcione como uma calculadora simples com menu.

O programa deve exibir repetidamente as seguintes opções:

1: soma
2: subtração
3: multiplicação
4: divisão
0: sair
Ao escolher uma operação, o usuário deve informar dois números, e o programa deve exibir o resultado correspondente.

O menu deve continuar sendo exibido até que o usuário escolha a opção 0.

Requisitos:
utilizar while para manter o programa em execução
utilizar if/elif/else para tratar as opções do menu
tratar divisão por zero
informar quando a opção digitada for inválida
"""

while True:
    print("\n»»»»»»» MENU «««««««" \
    "\n1: soma" \
    "\n2: subtração" \
    "\n3: multiplicação" \
    "\n4: divisão" \
    "\n0: sair")

    option = int(input("\nDigite a opção escolhida: "))

    if option == 1:
        print("\n» Você selecionou SOMA")
        number1 = float(input("Digite o primeiro número: "))
        number2 = float(input("Digite o segundo número: "))

        print(f"\nResultado: {number1} + {number2} = {number1 + number2}")
    elif option == 2:
        print("\n» Você selecionou SUBTRAÇÃO")
        number1 = float(input("Digite o primeiro número: "))
        number2 = float(input("Digite o segundo número: "))

        print(f"\nResultado: {number1} - {number2} = {number1 - number2}")

    elif option == 3:
        print("\n» Você selecionou MULTIPLICAÇÃO")
        number1 = float(input("Digite o primeiro número: "))
        number2 = float(input("Digite o segundo número: "))

        print(f"\nResultado: {number1} * {number2} = {number1 * number2}")

    elif option == 4:
        print("\n» Você selecionou DIVISÃO")
        number1 = float(input("Digite o primeiro número: "))
        number2 = float(input("Digite o segundo número: "))

        print(f"\nResultado: {number1} / {number2} = {number1 / number2}")

    elif option == 0:
        print("Obrigada, tchauzinho!")
        break

    else:
        print("\n» Opção inválida, selecione alguma opção do MENU.")