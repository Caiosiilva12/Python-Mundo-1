'''Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área 
e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².'''

larg = float(input('Informe a largura da parede? '))
alt = float(input('Informe a altura da parede? '))
area  = larg * alt
tinta = area / 2
print('A área da parede para ser pintada é {:.2f}'.format(area))
print('A quantidade de tinta para pintar é {:.2f}L'.format(tinta))
