'''
5. Leia um vetor de 10 posic¸ ˜oes. Contar e escrever quantos valores pares ele possui.
'''

vetor = [0,0,0,0,0,0,0,0,0,0]
count = 0

for i in range(10):
    num = float(input("Digite um número real: "))
    vetor[i] = num
    # if(v % 2 == 0): count += 1     -> Poderia usar aqui direto também.

for v in vetor:
    if(v % 2 == 0):
        count += 1


print(count)

# ps.: acho que esse leia é pra eu inventar um, mas deixei pro usuario inserir
