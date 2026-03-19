"""
2. Peça um número e verifique:

se está entre 10 e 50 (inclusive);
se é menor que 10;
se é maior que 50.
"""

number = int(input("Digite um numero: "))

if number <= 50 and number >= 10:
    print(number, "esta entre 10 e 50")

elif number < 10:
    print (number, "é menor que 10")

else:
    print(number, "é maior que 50")
