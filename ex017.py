'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
calcule e mostre o comprimento da hipotenusa.'''

import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai ter o comprimento de {:.2f}'.format(hi))
