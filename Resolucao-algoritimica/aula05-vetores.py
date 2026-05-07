# Vetores

# armazenar um conjunto de dados de uma mesma estrutura

# ordenado, estatico (nao muda de tamanho), homogeneo (mesmo tipo)

# Pratica 1
numeros = [5,7,12,2,9,21]

print(numeros)
for i in numeros:
    print(i)

# Pratica 2
numeros[1] = 17
numeros[3] = 22

print(numeros)

numeros[2] = 1
numeros[4] = 29

print(numeros)

# Pratica 3
sum = numeros[-1] + numeros[4]

sub = numeros[3] - numeros[1]

multiplication = numeros[0] * numeros[5]

division = numeros[3] / numeros[2]

print(f"soma: {sum}\nsubtração: {sub}\nmultiplicação: {multiplication}\ndivisão: {division}")

# Pratica 4
i = 0
while i < len(numeros):
    print(numeros[i] * 2)
    i += 1


# DESAFIO
'''
Implemente um programa em Python para verificar quantos números
uma aposta acertou na Mega Sena. O programa deve ler do teclado
os 6 números apostados e comparar com os 6 números sorteados.
Ao final, o programa deve exibir os números sorteados, números
jogados e quantidade de acertos.

Obs: Faça essa atividade usando apenas os conceitos de vetores, sem
utilizar nenhuma funcionalidade de listas.
'''

import random

while True:
    print("\nVamos jogar! ")

    perdeu = False
    megaSena = ["","","","","",""]
    aposta = ["","","","","",""]

    for i in range(len(megaSena)):
        megaSena[i] = str(random.randint(0,100))


    for i in range(len(aposta)):
        numAposta = input(str("\nDigite um número da Mega Sena: "))
        aposta[i] = numAposta

    for i in range(len(aposta)):
        if(aposta[i] != megaSena[i] and not perdeu):
            perdeu = True
    
    print(f"Você jogou: {aposta}\nA mega era: {megaSena}")

    if(perdeu):
        print("\nNão foi dessa vez :(")
    else:
        print("\nPARABÉNS!! Você foi o sortudo da vez!")
    

    opcao = input("\nDeseja jogar novamente? (s/n): ")
    while opcao != "s" and opcao != "n":
        opcao = input("\nDeseja jogar novamente? (s/n): ")

    if(opcao == "n"):
        print("\nTchau!")
        break
    