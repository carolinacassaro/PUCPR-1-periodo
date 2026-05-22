
'''
1. Escreva uma função chamada "imprimir_nome" que imprime o seu nome.
'''
def imprimir_nome():
    print("Carolina")

imprimir_nome()

'''
2. Escreva uma função chamada "maior" que receba três números como parâmetros e
retorne o maior entre eles.
'''
def maior(n1, n2, n3):
    if(n1>n2 and n1>n3):
        return n1
    elif(n2>n1 and n2>n3):
        return n2
    else:
        return n3
    
print(maior(1,2,3))

'''
3. Escreva uma função chamada "criar_vetor" que retorna um vetor preenchido com zeros
de tamanho 5.
'''
def criar_vetor():
    return [0,0,0,0,0]

vetor5 = criar_vetor()

'''
4. Escreva uma função chamada "media" que receba uma lista de números como
parâmetro e retorne a média desses números.
'''
def media(lista):
    return sum(lista)/len(lista)

for n in range(5):
    vetor5[n] = n+2 # simulando as notas

print(vetor5)
print(media(vetor5))

'''
5. Escreva uma função chamada "inverter" que receba uma string como parâmetro e
imprime a string invertida.
'''
def inverter(string):
    print(string[::-1])

inverter("Inverte a String")

'''
6. Escreva uma função chamada "imprime_diagonal" que recebe uma matriz de tamanho
3x3 preenchida com valores quaisquer, e imprime os valores na diagonal principal.
'''

def imprime_diagonal(matriz):
    for linha in range(3):
        for coluna in range(3):
            if(linha == coluna):
                print(matriz[linha][coluna])
    

matriz = [
    [1,0,0],
    [0,2,0],
    [0,0,3]
]

imprime_diagonal(matriz)