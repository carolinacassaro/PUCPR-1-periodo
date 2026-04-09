# FOR

# other languages offer 2 possibilities:
    # for <value> in <range>
    # for <element> in <vector>

# range(first i value, final i value, i behavior)

# i is 0 for standart
# final range value is not included

for i in range (5):
    print(i) # output: 0,1,2,3,4

print ("\nAtividade 1\n")

for i in range(1,11):
    print(i)

for i in range(10,0,-1):
    print(i)

print ("\nAtividade 2\n")

palavra = input("Digite uma palavra que inicia em vogal: ")

vogais = frozenset('aeiouAEIOU')

while palavra[0] != "a" and palavra[0] != "e" and palavra[0] != "i" and palavra[0] != "o" and palavra[0] != "u":
    palavra = input("Errado! Digite uma palavra que inicia em vogal: ")

for letra in palavra:
    print(letra)
