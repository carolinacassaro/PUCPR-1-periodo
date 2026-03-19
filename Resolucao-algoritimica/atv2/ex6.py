"""
6. [DESAFIO - não é obrigatório] Peça os três lados de uma figura. Primeiro, verifique se esses valores podem formar um triângulo.

⚠️Lembre-se: a soma de dois lados deve ser sempre maior que o terceiro.

Se for possível formar um triângulo, classifique-o:

Equilátero: todos os lados têm o mesmo tamanho.
Isósceles: dois lados têm o mesmo tamanho.
Escaleno: todos os lados são diferentes.

Além disso, verifique se o triângulo é retângulo:

⚠️Um triângulo é retângulo quando o quadrado do maior lado é igual à soma dos quadrados dos outros dois lados.

Caso os valores não formem um triângulo, informe isso ao usuário.
"""

lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    if lado1 == lado2 and lado2 == lado3:
        classificacao = "equilátero"
    elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
        classificacao = "escaleno"
    else:
        classificacao = "isóceles"

    if lado1 > lado2 and lado1 > lado3:
        maior_lado = lado1
        soma_quadrado_catetos = lado2**2 + lado3**2
    elif lado2 > lado1 and lado2 > lado3:
        maior_lado = lado2
        soma_quadrado_catetos = lado1**2 + lado3**2
    else: 
        maior_lado = lado3
        soma_quadrado_catetos = lado1**2 + lado2**2

    if maior_lado**2 == soma_quadrado_catetos:
        isRetangulo = "é retângulo"
    else:
        isRetangulo = "não é retângulo"
    print(f"É possivel formar um triangulo {classificacao} e {isRetangulo}")

else:
    print("Não é possível formar um triângulo com esses valores de lado")