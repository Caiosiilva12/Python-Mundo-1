'''Faça um programa que leia um ano qualquer e mostre se ele é bissexto.'''

from datetime import date
ano = int(input('Informe o ano qualquer ou digite "0" (zero) para o ano atual: ').strip())
if ano == 0:
    ano = date.today().year
    if(ano % 4 == 0):
        print('{} é ano bissexto'.format(ano))
        if(ano % 100 == 0):
            print('{} é ano bissexto'.format(ano))
        else:
            print('{} Não é ano bissexto'.format(ano))
    else:
        print('{} Não é ano bissexto'.format(ano))
else:
    print('{} Não é ano bissexto'.format(ano))




'''REVISAR A ESTRUTURA DO CÓDIGO!'''

