'''Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a
quantidade de dias pelos os quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00
por dia e R$0,15 por km rodado.'''

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos KM percorridos? '))
pago1 = dias * km
print('O total a pagar do aluguel é: R${:.2f}'.format(pago1))
pago2 = (dias * 60) + (km * 0.15)
print('O total a pagar por km é: R${:.2f}'.format(pago2))
