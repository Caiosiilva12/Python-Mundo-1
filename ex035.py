'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não
formar um triângulo.'''

r1 = float(input('Insira o primeiro valor da reta: '))
r2 = float(input('Insira o segundo valor da reta: '))
r3 = float(input('Insira o terceiro valor da reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('forma um triângulo')
else:
    print('Não forma um triângulo')
