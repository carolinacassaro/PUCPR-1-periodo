'''
Crie um algoritmo que peça ao usuário para informar 5 valores inteiros
positivos e armazene-os em uma lista com nome qualquer. Em seguida,
crie uma nova lista ordenada dos valores e uma nova lista com os valores
ordenados em ordem inversa. Imprima na tela:
a. As três listas
b. O tamanho da lista
c. O menor valor informado
d. O maior valor informado
e. A soma de todos os valores da lista
'''


valores = []

for i in range(5):
    valor = input("Digite o valor inteiro: ")
    valores.append(valor)

valoresOrdenados = sorted(valores)
valoresOrdenadosInversos = list(reversed(valoresOrdenados))

print(valores)
print(valoresOrdenados)
print(valoresOrdenadosInversos)