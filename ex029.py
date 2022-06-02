'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem 
dizendo que ele foi multado.
A multa vai custar R$7,00 por cada km acima do limite.'''

v = float(input('Informe a velocidade detectado: '))
m = (v - 80) * 7
if v > 80:
    print('ATENÇÃO: Você foi multado. O valor da multa a pagar é R${:.2f}'.format(m))
else:
    print('BOA VIAGEM!')
