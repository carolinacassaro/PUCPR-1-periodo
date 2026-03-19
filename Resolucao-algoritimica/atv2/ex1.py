
'''
Você está em uma floresta e precisa escolher um caminho para seguir. Você pode
escolher: esquerda ou direita.
➔ Se escolher o caminho da esquerda você encontrará um rio. Você deverá decidir:
atravessar ou voltar.
➔ Se escolher o caminho da direita você encontrará uma montanha. Você deverá
decidir: subir ou voltar.
Caminho da esquerda:
➔ Se atravessar - você chega a uma vila segura
➔ Se voltar - você permanece perdido na floresta
Caminho da direita:
➔ Se subir - você encontra um tesouro no topo
➔ Se voltar - você permanece perdido na floresta
󰱢Implemente um programa que simule essa decisão e mostre o resultado final ao usuário
'''

print("Você está em uma floresta e precisa escolher um caminho para seguir.")

while True:
    escolha1 = input("Você escolhe o caminho da esquerda ou da direita? (e/d): ")

    if escolha1 != "e" and escolha1 != "d":
        print("Digite um valor válido!")
    elif escolha1 == "e":
        while True:
            escolha2 = input("Voce acabou de encontrar um rio, deseja atravessar ou voltar? (a/v): ")

            if escolha2 != "a" and escolha2 != "v":
                print("Digite um valor válido!")
                
            elif escolha2 == "a" :
                print("Voce chegou numa vila segura")
                break
            else:
                break
        if escolha2 == "v":
            print("Voce voltou.")
        else:
            break

    elif escolha1 == "d":
        while True:

            escolha2 = input("Voce acabou de encontrar uma montanha, deseja subir ou voltar? (s/v): ")

            if escolha2 != "s" and escolha2 != "v":
                print("Digite um valor válido!")

            elif escolha2 == "s" :
                print("Voce encontrou um tesouro")
                break
            else:
                break
        if escolha2 == "v":
            print("Voce voltou!")
        else:
            break
