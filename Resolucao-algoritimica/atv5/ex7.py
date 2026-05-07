'''
7. Escreva um programa que leia 10 n ´umeros inteiros e os armazene em um vetor. Imprima
o vetor, o maior elemento e a posic¸ ˜ao que ele se encontra.
'''

vetor = [0,0,0,0,0,0,0,0,0,0]
maior = 0
posicao = 0

for i in range(10):
    num = int(input("Digite um número real: "))
    vetor[i] = num
    if(vetor[i]>maior):
        maior = vetor[i]
        posicao = i


print(vetor)
print(f"o maior é {maior} e está na posição: {posicao}")
