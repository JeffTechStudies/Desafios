'''
Escreva um programa que leia um numero N inteiro qualquer e mostre na tela os N primeiros elementos de uma
SEQUENCIA DE FIBONACCI.
ex. 0 > 1 > 1 > 2 > 3 > 5 > 8
'''

print(30*'\033[34m*\033[m')
print('{:^30}'.format('- Sequência Fibonacci -'))
print(30*'\033[34m*\033[m')
Num = int(input('Quantos números da sequecia deseja visualizar? '))
n1 = int(0)
n2 = int(1)
print('')
while Num > 0:
    print(n1, end=' - ')
    print(n2, end=' - ')
    Num -= 2
    n1 += n2
    n2 += n1
print('FIM ')
print('')
