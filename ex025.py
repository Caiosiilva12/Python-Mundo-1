'''Crie um programa que leia o nome de uma pessoa e diga se ela tem o "SILVA" no nome.'''

nome = str(input('Digite o seu nome completo: ')).strip()
print('O seu nome tem Silva? {}'.format('Silva' in nome))
print('O seu nome tem Silva? {}'.format('SILVA' in nome.upper()))
print('O seu nome tem Silva? {}'.format('silva' in nome.lower()))
print('O seu nome tem Silva? {}'.format('Silva' in nome.capitalize()))
