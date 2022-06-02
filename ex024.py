'''Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO" '''

cidade = str(input('Em que cidade você nasceu? ')).strip()
print(cidade [:5].upper() == 'SANTO')
print(cidade [:5].lower() == 'santo')
print(cidade [:5].capitalize() == 'Santo')
