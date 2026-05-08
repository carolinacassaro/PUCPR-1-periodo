# Principal diferença com Vetores: lista é dinâmica e aloca mais espaço da memória

# -- Métodos da lista: --------------------------
list = []
value = 0
index = 0


list.insert(index, value) # insere naquele index e empurra os outros pra direita

list.append(value) # adiciona como 1 item no final da lista

list.extend(list) # desempacota e adiciona cada item

list.remove(value) # remove um valor pelo valor

list.pop(index) # remove um valor por um index da lista e retorna esse valor
    ## obs.: se nao colocar parametro remove o ultimo valor.


'''
Crie um algoritmo que possua duas listas vazias chamadas
numerosJogador1 e numerosJogador2. Em seguida, randomize um
número entre 1 e 6 (vamos simular um dado) e armazene o valor na lista.
Repita esse processo 3 vezes (como se 3 dados tivessem sido jogados)
para cada um dos jogadores. Por último, some os valores de cada
jogador, e exiba na tela qual jogador foi o vencedor. Vence aquele que
tiver a soma com maior número.
'''

import random

numerosJogador1 = []

numerosJogador2 = []

for i in range(3):
    numerosJogador1.append(random.randint(1,6))
    numerosJogador2.append(random.randint(1,6))

sum1 = sum(numerosJogador1)
sum2 = sum(numerosJogador2)

if (sum1 > sum2):
    print(f"O jogador 1 é o vencedor por {sum1} X {sum2}")
else:
    print(f"O jogador 2 é o vencedor por {sum2} X {sum1}")


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