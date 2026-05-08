'''
5. Escreva um programa que crie uma lista de palavras e imprima a palavra mais
longa e a palavra mais curta da lista.
'''
lista = []
maior = ""

for i in range(3):
    palavra = input("Insira uma palavra: ")
    lista.append(palavra)

    if (i == 0):
        maior = palavra
        menor = palavra

    if (len(palavra) > len(maior)):
        maior = palavra
    elif (len(palavra) < len(menor)):
        menor = palavra

print(f"A maior palavra é: {maior} e a menor: {menor}")