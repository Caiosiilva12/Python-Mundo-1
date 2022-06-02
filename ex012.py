'''Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço,
com 5% de desconto.'''

produto = float(input('Informe o valor do produto R$: '))
desc = produto - (produto * 0.05)
print(desc)
