"""
3. Implemente um programa em Python para ler do teclado números.
Caso o usuário forneça um número igual a -1, o programa deve
fornecer a média dos números e encerrar;
"""

number = int(input("Digite um número: "))
sum = 0
counter = 0

while number != -1:
    sum += number
    counter += 1
    number = int(input("Digite um número: "))

average = sum/counter

print("média: ", average)

