'''
2. Escreva um programa que peça ao usuário três números e os armazene em uma
lista. Em seguida, imprima a lista na tela.
'''

lista = []

for i in range(3):
    num = float(input("Digite um número: "))

    lista.append(num)

print(lista)
