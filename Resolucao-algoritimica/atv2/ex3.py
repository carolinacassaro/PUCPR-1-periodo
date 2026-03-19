"""
3. Peça um ano e verifique se ele é bissexto. Um ano é bissexto se:

for divisível por 4 e não for divisível por 100 ou for divisível por 400.
"""

year = int(input("Digite um ano: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(year, "é um ano bissexto!")
else:
    print(year, "não é um ano bissexto.")