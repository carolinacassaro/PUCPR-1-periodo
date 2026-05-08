'''
9. Escreva um programa que crie uma lista com as letras do alfabeto e embaralhe
suas posições. Em seguida, peça ao usuário para adivinhar a posição correta de
uma determinada letra e informe se ele acertou ou errou.
'''
import random

alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

alfabetoRandomizado = alfabeto
random.shuffle(alfabetoRandomizado)

letra = random.choice(alfabetoRandomizado)
indexCorreto = alfabetoRandomizado.index(letra)

index = int(input(f"Qual a posição da letra {letra}: "))

if(indexCorreto == index):
    print("Você acertou!")
else:
        print(f"Você errou. Era {indexCorreto}")