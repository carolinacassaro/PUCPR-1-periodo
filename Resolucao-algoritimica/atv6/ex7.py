'''
7. Escreva um programa que crie uma lista com os números de 1 a 100. Em seguida,
imprima apenas os números pares da lista.
'''

lista = []
pares = []

for i in range(1, 101):
    lista.append(i)

    if (i%2 == 0):
        pares.append(i)
        # ou já imprime direto com print se não precisar armazenar

print(pares)