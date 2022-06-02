'''Crie um programa que leia o nome completo de uma pessoa e mostre:
- Nome com todas as letras maiúsculas.
- Nome com todas as letras minúsculas.
- Quantas letras tem o primeiro nome.'''

nome = str(input('Nome completo: ')).strip()
print('O seu nome em maiúsculo: {}'.format(nome.upper()))
print('O seu nome em minúsculo: {}'.format(nome.lower()))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
