'''
4. Fac¸a um programa que leia um vetor de 8 posic¸ ˜oes e, em seguida, leia tamb ´em dois va-
lores X e Y quaisquer correspondentes a duas posic¸ ˜oes no vetor. Ao final seu programa
devera´ escrever a soma dos valores encontrados nas respectivas posic¸ ˜oes X e Y .
'''

vetor = [0,0,0,0,0,0,0,0]

for i in range(8):
    num = int(input("Digite um número: "))
    vetor[i] = num

X = int(input("Digite um valor de 0-7: "))
Y = int(input("Digite outro valor de 0-7: "))

sum = vetor[X] + vetor[Y]

print(f"Soma: {sum}")

# ps.: acho que esse leia é pra eu inventar um, mas deixei pro usuario inserir
