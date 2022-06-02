'''Faça um programa que leia algo pelo o teclado e mostre na tela o seu tipo primitivo
e todas as informações possíveis sobre ela.'''

msg = input('Digite algo: ')
print('É numérico?', msg.isnumeric())
print('É alfabético?',msg.isalpha())
print('É alfanumérico?',msg.isalnum())
print('Está em maiúsculo?',msg.isupper())
print('Está em minúsculo?',msg.islower())
print('Está com a primeira letra em maiúsculo?',msg.istitle())
