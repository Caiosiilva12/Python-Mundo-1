'''Crie um programa que leia quanto dinheiro uma pessoa tem na carteira 
e mostre quantos dólares ela pode comprar.
Considere US$1,00 = R$3,27'''

real = float(input('Informe quanto de valor possui na carteira R$: '))
dolar = real / 5.61
print('Com R${:.2f} você possui US${:.2f} dólares'.format(real, dolar))
