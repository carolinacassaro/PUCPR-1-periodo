"""
2. Crie uma função chamada e_palindromo que receba uma string como
parâmetro e retorne True se a string for um palíndromo (ou seja, se lida de trás
para frente for igual à original) e False caso contrário.
"""

def e_palindromo(string):
    if(string == string[::-1]):
        return True
    return False


string = input("Digite: ")
print(e_palindromo(string))