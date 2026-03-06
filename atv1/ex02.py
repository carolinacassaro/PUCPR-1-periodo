"""
2. Escreva um algoritmo em Python para calcular o valor, em reais, que deve ser pago por
um cliente de uma locadora de carros. Sabe-se que o valor de cada carro é R$ 100,00.
Solicite ao usuário quantos carros ele gostaria de alugar e imprima o valor total da
locação de todos os carros.
"""

cars = int(input("Digite quantos carros você quer alugar: "))

value = float(cars*100)

print (f"Seu total será de {value:.2f} reais.")