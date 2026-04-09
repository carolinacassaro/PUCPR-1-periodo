"""
4. Peça ao usuário que digite um valor referente à quantidade de linhas. Em seguida, utilize
for para exibir o seguinte padrão: (Exemplo para usuário que digitou 5)
"""

numero4 = int(input("Digite o número de linhas: "))

for i in range(1,numero4+1):
    print()
    for n in range(1,i+1):
        print(f" {n} ", end="")

