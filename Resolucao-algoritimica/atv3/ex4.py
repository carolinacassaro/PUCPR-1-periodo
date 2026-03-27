"""
4. Escreva um programa que receba 10 números do teclado e exiba a
quantidade de números pares e ímpares lidos.
"""
counter = 0
even = 0
odd = 0

while counter < 10:
    number = int(input("Digite um número: "))
    if number % 2 == 0:
        even += 1
    else:
        odd += 1

    counter += 1

print("Pares:", even)
print("Ímpares:", odd)