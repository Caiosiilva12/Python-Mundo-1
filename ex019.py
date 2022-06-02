'''Um professor quer sortear um dos seus alunos para apagar o quadro. Faça um programa que ajude ele,
lendo o nome deles e escrevendo o nome escolhido.'''

import random
a1 = str(input('Nome do primeiro aluno(a): '))
a2 = str(input('Nome do segundo aluno(a): '))
a3 = str(input('Nome do terceiro aluno(a): '))
a4 = str(input('Nome do quarto aluno(a): '))
lista = [a1, a2, a3, a4]
aluno = random.choice(lista)
print('O(a) aluno(a) sorteado foi {}'.format(aluno))
