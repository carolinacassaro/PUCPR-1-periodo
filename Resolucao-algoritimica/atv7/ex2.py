'''
2. Leia uma matriz 4 x 4, imprima a matriz e retorne a localização (linha e a
coluna) do maior valor.
'''

matriz = [
    [2,2,2,2],
    [2,2,2,2],
    [2,2,2,2],
    [2,2,2,2]
]

maior = 0


for linha in range(4):
    for coluna in range(4):
        valor = float(input("Digite um valor: "))
        matriz[linha][coluna] = valor
        if(valor>maior):
            maior = valor
            posicao = f"linha: {linha}; coluna: {coluna}"

for m in matriz:
    print(m)

print(posicao)

