"""
Nivel 1: facil
O programa deve aceitar uma expressão aritmética simples, contendo:

dois números
um único operador
Exemplos de entradas aceitas:

2 + 5
10 - 4
3 * 8
20 / 5
O programa deve identificar os dois operandos e o operador, realizar o cálculo correspondente e exibir o resultado.
"""

equation = str(input("Digite sua operação: "))

format = equation.replace(" ", "")

i = 0
operadores = ["+", "-", "*", "/"]

while i < len(format):
    if format[i] in operadores:
        if i == len(format) -1:
            equation = str(input("Operação inválida. Digite sua operação: "))
            format = equation.replace(" ", "")

            i = 0
        else:
            if format[i] == "+":
                if i == len(format) -1:
                    equation = str(input("Operação inválida. Digite sua operação: "))
                    format = equation.replace(" ", "")

                    i = 0
                number1 = float(format[:i])
                number2 = float(format[i+1:])

                print(f"SOMA: {number1} + {number2} = {number1 + number2}")
                i = len(format)

            elif format[i] == "-":
                number1 = float(format[:i])
                number2 = float(format[i+1:])

                print(f"SUBTRAÇÃO: {number1} - {number2} = {number1 - number2}")
                i = len(format)

            elif format[i] == "*":
                number1 = float(format[:i])
                number2 = float(format[i+1:])

                print(f"MULTIPLICAÇÃO: {number1} * {number2} = {number1 * number2}")
                i = len(format)

            elif format[i] == "/":
                number1 = float(format[:i])
                number2 = float(format[i+1:])

                print(f"DIVISÃO: {number1} / {number2} = {number1 / number2}")
                i = len(format) # or use break

    elif format[i].isalnum():
        if i == len(format) - 1:
            equation = str(input("Operação inválida. Digite sua operação: "))
            format = equation.replace(" ", "")

            i = 0
        else:
            i += 1
    else:
        print(equation)
        equation = str(input("Operação inválida. Digite sua operação: "))
        format = equation.replace(" ", "")

        i = 0


