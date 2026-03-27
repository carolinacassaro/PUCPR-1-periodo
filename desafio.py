
print ("Bem-vindo à calculadora!")

print("Para and use &\nPara or use |\nPara not use !\nPara implicação use >\nPara bi-implicação use =")

operacao = input("Insira sua operação seguindo as ordens: ")


# percorrer e separar os parenteses

# ands, ors, implicacoes

# usar string.split para separar operadores

# ((p&q) | (p | !(q>p)))

# list = []
# list.apped(addItem)


operacaoList = tuple(operacao)

for i, item in enumerate(operacaoList):
    if item == "(":
        start = i
        

        

        
                

