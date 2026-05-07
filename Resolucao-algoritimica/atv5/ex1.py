'''

3. Ler um conjunto de n ´umeros reais, armazenando-o em vetor e calcular o quadrado das
componentes deste vetor, armazenando o resultado em outro vetor. Os conjuntos t ˆem 10
elementos cada. Imprimir os conjuntos.
4. Fac¸a um programa que leia um vetor de 8 posic¸ ˜oes e, em seguida, leia tamb ´em dois va-
lores X e Y quaisquer correspondentes a duas posic¸ ˜oes no vetor. Ao final seu programa
devera´ escrever a soma dos valores encontrados nas respectivas posic¸ ˜oes X e Y .
5. Leia um vetor de 10 posic¸ ˜oes. Contar e escrever quantos valores pares ele possui.
6. Fac¸a um programa que receba do usu ´ario um vetor com 10 posic¸ ˜oes. Em seguida dever ´a
ser impresso o maior e o menor elemento do vetor.
7. Escreva um programa que leia 10 n ´umeros inteiros e os armazene em um vetor. Imprima
o vetor, o maior elemento e a posic¸ ˜ao que ele se encontra.
8. Fac¸a um programa para ler a nota da prova de 15 alunos e armazene num vetor, calcule
e imprima a m ´edia geral.
9. Fac¸a um programa que preencha um vetor com 10 n ´umeros reais, calcule e mostre a
quantidade de n ´umeros negativos e a soma dos n ´umeros positivos desse vetor.
10. Fazer um programa para ler 5 valores e, em seguida, mostrar todos os valores lidos
juntamente com o maior, o menor e a m ´edia dos valores.
11. Fazer um programa para ler 5 valores e, em seguida, mostrar a posic¸ ˜ao onde se encon-
tram o maior e o menor valor
'''

'''
Fac¸a um programa que possua um vetor denominado A que armazene 6 n ´umeros intei-
ros. O programa deve executar os seguintes passos:
(a) Atribua os seguintes valores a esse vetor: 1, 0, 5, -2, -5, 7.
(b) Armazene em uma vari ´avel inteira (simples) a soma entre os valores das posic¸ ˜oes
A[0], A[1] e A[5] do vetor e mostre na tela esta soma.
(c) Modifique o vetor na posic¸ ˜ao 4, atribuindo a esta posic¸ ˜ao o valor 100.
(d) Mostre na tela cada valor do vetor A, um em cada linha.
'''

A = [1, 0, 5, -2, -5, 7]

sum = A[0] + A[1] + A[5] 

print(f"Soma: {sum}")

A[4] = 100

for a in A:
    print(a)