"""
Peça ao usuário que digite uma palavra. A palavra digitada precisa ter no mínimo 3 letras e no máximo 10.
Ao final, imprima palavra digitada e a quantidade de letras.
"""

word = input("Digite uma palavra de 3 a 10 letras: ")

while len(word) < 3 or len(word) > 10:
    word = input("Digite uma palavra de 3 a 10 letras: ")

print("A palavra", word, "tem", len(word), "letras.")
