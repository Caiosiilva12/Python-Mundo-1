'''Crie um programa que leia um número real qualquer pelo o teclado e mostre na tela a sua porção inteira.
Ex: Digite um número: 6.127
O número 6.127 tem a parte inteira 6.'''

from math import trunc
num = float(input('Digite um número: '))
print('O número {} tem a parte interira {}'.format(num, trunc(num)))