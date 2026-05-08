'''
4. Escreva um programa que crie uma lista com os números de 1 a 10 e os imprima
na tela em ordem reversa.
'''

lista = []
for i in range(1, 11):
    lista.append(i)

listaReversa = list(reversed(lista))

print(f"Lista normal ordenada: {lista}")
print(f"Lista reversa: {listaReversa}")