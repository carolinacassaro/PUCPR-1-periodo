'''
3. Ler um conjunto de numeros reais, armazenando-o em vetor e calcular o quadrado das
componentes deste vetor, armazenando o resultado em outro vetor. Os conjuntos t ˆem 10
elementos cada. Imprimir os conjuntos.
'''

reais = [0,0,0,0,0,0,0,0,0,0]
reaisQuadrados = [0,0,0,0,0,0,0,0,0,0]

for i in range(10):
    num = float(input("Digite um número real: "))
    reais[i] = num
    reaisQuadrados[i] = num**2


print(reais)
print(reaisQuadrados)