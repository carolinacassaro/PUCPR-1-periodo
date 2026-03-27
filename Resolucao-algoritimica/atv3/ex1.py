"""
1. Implemente um programa em Python para ler do teclado a nota de
um aluno. Verifique se o valor lido é uma nota válida (entre 0 e 10).
Se não for, ler este valor até que a mesma seja válida;
"""

grade = float(input("Digite sua nota: "))

while grade < 0 or grade > 10:
    grade = float(input("Nota inválida! Digite sua nota (0 a 10): "))

print("Sua nota é válida:", grade)