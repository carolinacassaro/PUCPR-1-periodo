"""
6. Desenvolvimento de uma calculadora em Python com menu de opções

Implemente um programa em Python que funcione como uma calculadora simples com menu.

O programa deve exibir repetidamente as seguintes opções:

1: soma
2: subtração
3: multiplicação
4: divisão
0: sair
Ao escolher uma operação, o usuário deve informar dois números, e o programa deve exibir o resultado correspondente.

O menu deve continuar sendo exibido até que o usuário escolha a opção 0.

Requisitos:
utilizar while para manter o programa em execução
utilizar if/elif/else para tratar as opções do menu
tratar divisão por zero
informar quando a opção digitada for inválida
6.1 [DESAFIO com expressão completa]

Crie uma nova versão da calculadora sem menu de opções, em que o usuário digita diretamente uma expressão aritmética para ser resolvida pelo programa.

Escolha um dos níveis abaixo para implementar, de acordo com o grau de dificuldade desejado.

Nível 1: Fácil

O programa deve aceitar uma expressão aritmética simples, contendo:

dois números
um único operador
Exemplos de entradas aceitas:

2 + 5
10 - 4
3 * 8
20 / 5
O programa deve identificar os dois operandos e o operador, realizar o cálculo correspondente e exibir o resultado.

Nível 2: Intermediário

O programa deve aceitar uma expressão com quantidade ilimitada de números e operadores, por exemplo:

2 + 5 - 1
10 + 4 + 3
20 / 5 * 2
Nesta versão, a expressão deve ser resolvida da esquerda para a direita, sem respeitar a prioridade entre operadores.

Exemplo:

8 + 3 * 2
Resultado produzido pelo programa nessa versão:

8 + 3 = 11
11 * 2 = 22
Observação: nessa versão, a expressão será resolvida apenas na ordem em que aparece, o que pode gerar resultados diferentes da prioridade matemática usual.

Nível 3: Difícil

O programa deve aceitar uma expressão com quantidade ilimitada de números e operadores, por exemplo:

2 + 5 - 1
10 + 4 * 3
20 / 5 * 2
8 + 3 * 2
Nesta versão, o programa deve resolver a expressão respeitando a prioridade das operações, ou seja:

multiplicação e divisão antes
soma e subtração depois
Exemplo:

8 + 3 * 2
Resultado correto:

3 * 2 = 6
8 + 6 = 14
Nível 4: Muito Difícil

O programa deve aceitar uma expressão completa, incluindo:

vários números
vários operadores
uso de parênteses
Exemplos:

2 * (3 + 5 - 1)
(10 - 2) * 3
8 + 2 * (4 - 1)
Nesta versão, o programa deve resolver corretamente a expressão considerando:

os parênteses
a prioridade entre operadores
Regras gerais do desafio

a calculadora não deve utilizar menu de opções
o usuário deve digitar diretamente a expressão
o programa deve continuar funcionando até que seja digitado um comando de saída, como sair
o programa deve informar quando a expressão estiver em formato inválido
o programa deve tratar divisão por zero, quando necessário
"""