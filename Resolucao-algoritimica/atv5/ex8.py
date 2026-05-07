'''

8. Fac¸a um programa para ler a nota da prova de 15 alunos e armazene num vetor, calcule
e imprima a m ´edia geral.
'''

vetor = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
maior = 0
posicao = 0
sum = 0

for i in range(15):
    num = int(input(f"Digite a nota do aluno {i+1}: "))
    vetor[i] = num
    sum += vetor[i]

media = sum/15

print(f"A média geral é: {media}")