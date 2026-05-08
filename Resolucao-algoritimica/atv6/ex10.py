'''
10. Se você terminou os exercícios acima. Tente agora fazer o jogo da velha, mas
utilizando listas.
'''
import random

jogadas = ["pedra", "papel", "tesoura"]

print("Você jogará contra um bot. ")

while True:
    print("\n1- pedra, 2 - papel, 3 - tesoura")
    j1 = int(input("\nFaça sua jogada J1: ")) - 1

    if(len(jogadas)>= j1 and j1>=0):
        break

j2 = jogadas.index(random.choice(jogadas))

if (j1 == j2):
    print(f"\nEmpate. {jogadas[j1]} X {jogadas[j2]}")

elif (j1 == 0 and j2 == 2 or j1 == 1 and j2 == 0 or j1 == 2 and j2 == 1):
    print(f"\nVitoria do Jogador 1. {jogadas[j1]} X {jogadas[j2]}")

else:
    print(f"\nVitoria do Jogador 1. {jogadas[j1]} X {jogadas[j2]}")