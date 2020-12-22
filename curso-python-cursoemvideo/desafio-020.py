#desafio-020

import random

n1 = str(input('Digite o nome do primeiro grupo: '))
n2 = str(input('Digite o nome do segundo grupo:  '))
n3 = str(input('Digite o nome do terceiro grupo: '))
n4 = str(input('Digite o nome do quarto grupo:   '))

lista = [n1,n2,n3,n4]
random.shuffle(lista)

print('A ordem de apresentação é {} : '.format(lista))