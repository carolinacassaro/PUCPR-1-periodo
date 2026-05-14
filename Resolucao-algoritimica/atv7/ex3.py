'''
3. Faça um programa que leia uma matriz de 5 linhas e 4 colunas contendo as
seguintes informações sobre alunos de uma disciplina, sendo todas as
informações do tipo inteiro:
a. Primeira coluna: número de matrícula (use um inteiro)
b. Segunda coluna: media das provas
c. Terceira coluna: media dos trabalhos
d. Quarta coluna: nota final
Elabore um programa que:
a. Leia as três primeiras informações de cada aluno;
b. Calcule a nota final como sendo a soma da média das provas e da
média dos trabalhos;
c. Imprima a matrícula do aluno que obteve a maior nota final (assuma que só existe
uma maior nota).
'''

matriz = [
    [0,5,6,0],
    [1,3,7,0],
    [2,5,9,0],
    [3,7,4,0],
    [4,8,10,0]
]

maior = 0

for linha in range(4):
    media = matriz[linha][1] + matriz[linha][2]
    matriz[linha][3] = media

    if(media>maior):
        maior = media
        aluno = matriz[linha][0]

for m in matriz:
    print(m)

print(f"matricula: {aluno}")
            