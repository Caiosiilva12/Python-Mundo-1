'''Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, 
cobrando R$0,50 por km para viagens até 200km e R$0,45 para viagens mais longes.'''

d = float(input('Qual a distância que será percorrido: '))
if d <= 200:
    print('O valor a ser cobrado nessa distância é R${:.2f}'.format(d * 0.50))
else:
    print('O valor a ser cobrado nessa distância é R${:.2f}'.format(d * 0.45))
