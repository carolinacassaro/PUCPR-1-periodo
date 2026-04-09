"""
Exercicios:
1. Faça um programa que percorra os números de 1 até 100 e mostre apenas aqueles que
são múltiplos de 3 e, ao mesmo tempo, não são múltiplos de 5. Ao final, mostre também
quantos números atenderam a essa condição.
"""
soma = 0

for i in range(1,101):
    if i % 3 == 0 and i % 5 != 0:
        print(i)
        soma += 1

print(f"Quantidade de números: {soma}")