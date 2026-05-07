'''
6. Fac¸a um programa que receba do usu ´ario um vetor com 10 posic¸ ˜oes. Em seguida dever ´a
ser impresso o maior e o menor elemento do vetor.
'''

vetor = [0,0,0,0,0,0,0,0,0,0]
count = 0
maior = 0
menor = 0

for i in range(10):
    num = float(input("Digite um número real: "))
    vetor[i] = num
    if(i==0):
        maior = vetor[i]
        menor = vetor[i]
    else:
        if(vetor[i]>maior):
            maior = vetor[i]
        elif(vetor[i]<menor):
            menor = vetor[i]
    

print(f"O maior é: {maior} e o menor é: {menor}")