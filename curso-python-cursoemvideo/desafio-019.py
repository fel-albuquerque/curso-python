#desafio-019

import random

n1 = str(input('Digite o nome: '))
n2 = str(input ('Digite segundo nome: '))
n3 = str(input('Digite o terceiro nome: '))
n4 = str(input('Digite o quarto nome: '))

sort = [n1, n2, n3, n4]

print('o Nome sorteado é {}'.format(random.choice(sort)))