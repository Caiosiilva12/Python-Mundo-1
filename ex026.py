'''Faça um programa que leia uma frase pelo o teclado e mostre: 
- Quantas vezes aparece a letra "A". 
- Em que posição ela aparece a primeira vez. 
- Em que posição ela aparece a última vez. '''

frase = str(input('Digite uma frase: ')).strip().upper()
print('Quantas vezes aparece a letra "A"? {}'.format(frase.count('A')))
print('Em que posição ela aparece a primeira vez? {}'.format(frase.find('A') + 1))
print('Em que posição ela aparece a última vez? {}'.format(frase.rfind('A') + 1))
