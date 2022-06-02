'''Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.'''
aluno = str(input('Digita o nome do aluno: '))
nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))
media = (nota1 + nota2) / 2
print('A média do aluno {} é {}'.format(aluno, media))
