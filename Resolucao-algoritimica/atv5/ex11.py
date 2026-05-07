'''
11. Fazer um programa para ler 5 valores e, em seguida, mostrar a posic¸ ˜ao onde se encon-
tram o maior e o menor valor
'''

vetor = [0,0,0,0,0]
maior = 0
pM = 0
menor = 0
pm = 0

for i in range(5):
    num = float(input("Digite um número real: "))
    vetor[i] = num
    if(i==0):
        maior = vetor[i]
        pM = i
        menor = vetor[i]
        pm = i
    else:
        if(vetor[i]>maior):
            maior = vetor[i]
            pM = i
        elif(vetor[i]<menor):
            menor = vetor[i]
            pm = i


print(f"O maior é {maior} e sua posição é: {pM}")
print(f"O menor é {menor} e sua posição é: {pm}")