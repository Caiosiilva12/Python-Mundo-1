'''Faça um algoritmo que leia o salário de um funcionário e mostre o seu novo salário,
com o 15% de aumento.'''

salario = float(input('Informe o salario.R$: '))
aumento = salario + (salario * 0.15)
print('O salario anterior de {:.2f} Com 15% de aumento passará a ser de {:.2f}'.format(salario, aumento))
