# print("Imprima os números de 1 a 10 em ordem crescente")
# a = 1

# while a<=10:
#     print(a)
#     a += 1

# print("Imprima os números de 1 a 10 em ordem decrescente")

# b = 10

# while b>= 1:
#     print(b)
#     b -= 1

print("Solicite um valor entre 1 e 10 aousuário e imprima a tabuada desse número.")

number = int(input("Digite um número de 1 a 10: "))

c = 0

## while c<=9:
##     print(c, "*", number, "=", number*c)
##     c += 1

## Mas como podemos garantir que o usuário digite o valor correto?


while number < 1 or number >= 10:
    number = int(input("Número inválido, digite um número de 1 a 10 (exclusivo): "))

while c<=9:
    print(c, "*", number, "=", number*c)
    c += 1



print("Peça ao usuário que digite uma palavra. A palavra digitada precisa ter no mínimo 3 letras e no máximo 10. " \
"Ao final, imprima palavra digitada e a quantidade de letras.")

word = input("Digite uma palavra de 3 a 10 letras: ")

while len(word) < 3 or len(word) > 10:
    word = input("Digite uma palavra de 3 a 10 letras: ")

print("A palavra", word, "tem", len(word), "letras.")

# while True and While with flag

acesso = False # acesso é minha flag
answer = 0

while not acesso:
    if answer == 1:
        acesso = True
        print("acesso permitido")
    else:
        answer = int(input("Digite 1 para true e 0 para falso: "))