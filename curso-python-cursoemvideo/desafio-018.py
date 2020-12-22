#desafio-018

import math 

angulo =  float(input('Digite um valor para saber o seno, coseno e a tangente: '))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('Os angulos são SENO {:.2f} , COSSENO {:.2f} , TANGENTE {:.2f}'.format(seno, cosseno, tangente))