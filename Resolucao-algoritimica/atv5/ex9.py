'''
9. Fac¸a um programa que preencha um vetor com 10 n ´umeros reais, calcule e mostre a
quantidade de n ´umeros negativos e a soma dos n ´umeros positivos desse vetor.
'''

vetor = [0,0,0,0,0,0,0,0,0,0]
count = 0
sum = 0

for i in range(10):
    num = float(input(f"Digite um número: "))
    vetor[i] = num
    if(num<0):
        count += 1
    else:
        sum += num


print(f"Quantidade de negativos: {count}\nSoma dos positivos: {sum}")