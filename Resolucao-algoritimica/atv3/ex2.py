"""
2. Implemente um programa em Python para imprimir na tela o
somatório dos N primeiros números inteiros a partir do 1. Sendo N
lido do teclado;
"""

n = int(input("Digite um número inteiro: "))
x = 1
sum = 0

while x <= n:
    print(x, "+", sum)
    sum += x
    print(sum)
    x += 1

print("Somatório final:", sum)