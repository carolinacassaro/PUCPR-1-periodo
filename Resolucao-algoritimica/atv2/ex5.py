"""
5. Peça duas coordenadas (x, y) e verifique a posição do ponto em relação a um quadrado cujos vértices vão de (0,0) até (10, 10).

Se o ponto estiver estritamente dentro da região, mostre “Dentro do quadrado”.
Se estiver exatamente em uma das bordas, mostre “Na fronteira”.
Caso contrário, mostre “Fora do quadrado”.
"""

x = int(input("Digite a primeira coordenada (x): "))
y = int(input("Digite a segunda coordenada (y): "))

if ((x == 10 or x == 0) and (y <= 10 and y >= 0)) or ((y == 10 or y == 0) and (x <= 10 and x >= 0)):
    print("O ponto esta *na fronteira*")

elif x >= 0 and x <= 10 and y <= 10 and y >= 0:
    print("O ponto esta *dentro do quadrado*")

else:
    print("O ponto esta *fora do quadrado*")