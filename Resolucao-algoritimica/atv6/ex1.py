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