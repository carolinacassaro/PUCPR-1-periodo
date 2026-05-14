'''
1. Declare uma matriz 5 x 5. Preencha com 1 a diagonal principal e com 0 os
demais elementos. Escreva ao final a matriz obtida.
'''

matriz = [
    [2,2,2,2,2],
    [2,2,2,2,2],
    [2,2,2,2,2],
    [2,2,2,2,2],
    [2,2,2,2,2]
]

for linha in range(5):
    for coluna in range(5):
        if (linha == coluna):
            matriz[linha][coluna] = 1
        else:
            matriz[linha][coluna] = 0

for m in matriz:
    print(m)