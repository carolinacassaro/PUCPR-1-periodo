'''
1. Escreva um programa que crie uma lista com números aleatórios e a imprima na
tela.
'''

lista = []

while True:
    item = input("Adicione um item na lista: ")

    lista.append(item)

    continuar = input("Deseja adicionar mais itens? (s/n): ")

    if(continuar == 'n'):
        break


print(lista)