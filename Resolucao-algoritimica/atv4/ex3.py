
"""
3. Peça ao usuário um número inicial e um número final. Para cada número dentro desse
intervalo, exiba a tabuada dele de 1 até 10. Exemplo: início = 3, fim = 5 -> Output:
tabuado do 3, tabuada do 4 e tabuada do 5
"""

inicio = int(input("Digite o número inicial: "))
fim = int(input("Digite o número final: "))

for i in range(inicio, fim+1):
    print(f"\nTabuada de {i}:")
    for n in range(1,10):
        print(f"{n} * {i} = {n*i}")
