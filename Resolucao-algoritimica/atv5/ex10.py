'''
10. Fazer um programa para ler 5 valores e, em seguida, mostrar todos os valores lidos
juntamente com o maior, o menor e a m ´edia dos valores.
'''

vetor = [0,0,0,0,0]
maior = 0
menor = 0
sum = 0

for i in range(5):
    num = float(input("Digite um número real: "))
    vetor[i] = num
    sum += num
    if(i==0):
        maior = vetor[i]
        menor = vetor[i]
    else:
        if(vetor[i]>maior):
            maior = vetor[i]
        elif(vetor[i]<menor):
            menor = vetor[i]


media = sum/5

print(vetor)
print(f"O maior é: {maior}, enquanto o menor é: {menor}\nA média é: {media}")