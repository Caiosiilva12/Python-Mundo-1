'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
tentar descobrir qual foi o número escolhido pelo o computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

from random import randint
from time import sleep
pc = randint(0,5) #faz o pc pensar!
print('-=-'*30)
print('ANONNYMOUS: Ai mané, vou pensar em um número entre 0 e 5! Tente adivinhar se tu foi bom...')
print('-=-'*30)
jogador = int(input('Em que número pensei? '))
sleep(3) # O tempo usado para aguardar o resultado sair!
if jogador == pc:
    print('Muito bom! Você é esperto.')
else:
    print('Falhou!!! O número que escolhi foi {}'.format(pc))
