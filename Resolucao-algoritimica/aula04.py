# FOR

# other languages offer 2 possibilities:
    # for <value> in <range>
    # for <element> in <vector>

# range(first i value, final i value, i behavior)

# i is 0 for standart
# final range value is not included

for i in range (5):
    print(i) # output: 0,1,2,3,4

print ("\nAtividade 1\n")

for i in range(1,11):
    print(i)

for i in range(10,0,-1):
    print(i)

print ("\nAtividade 2\n")

palavra = input("Digite uma palavra que inicia em vogal: ")

vogais = frozenset('aeiouAEIOU')

while palavra[0] != "a" and palavra[0] != "e" and palavra[0] != "i" and palavra[0] != "o" and palavra[0] != "u":
    palavra = input("Errado! Digite uma palavra que inicia em vogal: ")

for letra in palavra:
    print(letra)

"""
Exercicios:
1. Faça um programa que percorra os números de 1 até 100 e mostre apenas aqueles que
são múltiplos de 3 e, ao mesmo tempo, não são múltiplos de 5. Ao final, mostre também
quantos números atenderam a essa condição.
"""

for i in range(1,101):
    if i % 3 == 0 and i % 5 != 0:
        print(i)

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


"""
3. Peça ao usuário um número inicial e um número final. Para cada número dentro desse
intervalo, exiba a tabuada dele de 1 até 10. Exemplo: início = 3, fim = 5 -> Output:
tabuado do 3, tabuada do 4 e tabuada do 5
"""

inicio = int(input("Digite o número inicial: "))
fim = int(input("Digite o número final: "))

for i in range(inicio, fim+1):
    print(f"\nTabuada de {i}:")
    for n in range(1,10):
        print(f"{n} * {i} = {n*i}")

    # print(f"{i} x 1 = {1*i}" 
    #       f"{i} x 2 = {2*i}"
    #       f"{i} x 3 = {3*i}"
    #       f"{i} x 4 = {4*i}"
    #       f"{i} x 5 = {5*i}"
    #       f"{i} x 6 = {6*i}"
    #       f"{i} x 7 = {7*i}"
    #       f"{i} x 8 = {8*i}"
    #       f"{i} x 9 = {9*i}")

"""
4. Peça ao usuário que digite um valor referente à quantidade de linhas. Em seguida, utilize
for para exibir o seguinte padrão: (Exemplo para usuário que digitou 5)
"""

numero4 = int(input("Digite o número de linhas: "))

for i in range(1,numero4+1):
    print()
    for n in range(1,i+1):
        print(f" {n} ", end="")

