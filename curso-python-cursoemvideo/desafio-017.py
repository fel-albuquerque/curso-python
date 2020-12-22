#desafio 017
#Maneira um
'''co = float(input('Digite o cateto oposto : '))
ca = float(input('Digite o cateto adjacente: '))

h = (co **2 + ca **2) ** (1/2)

print('O cateto oposto é {} , cateto adjacente é {} sua hipotenusa é {:.2f} :'.format(ca, co, h))'''

#maneira dois
#import math ou
from math import hypot
co = float(input('Digite o cateto oposto : '))
ca = float(input('Digite o cateto adjacente: '))

h = hypot(co, ca)

print ('O cateto oposto é {}, cateto adjacente {}, a hipotenusa é {:.2f} :'.format(co, ca, h))