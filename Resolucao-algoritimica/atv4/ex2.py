"""
2. Peça ao usuário um número inteiro positivo n. Não permita que o programa continue
caso o número não seja válido. Em seguida, calcule e exiba a soma de todos os números
de 1 até n. Ao final exiba a expressão aritmética completa, incluindo o resultado.
Exemplo: n = 5 -> Output: 1 + 2 + 3 + 4 + 5 = 15
"""

numero = str(input("Digite um número inteiro positivo: "))

while not numero.isdigit():
    numero = input("Valor inválido. Digite um número inteiro positivo: ")

numero = int(numero)

while numero < 0:
    numero = input("Valor inválido. Digite um número inteiro positivo: ")

    

soma = 0
expressao = ""

for i in range(1,numero+1):    
    soma += i
    if i == numero:
          print(f"{expressao}{i} = {soma}")

    else:
        expressao += f"{i} + "

