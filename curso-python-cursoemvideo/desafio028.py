#desafio 28

import random

chute = int(input('Acerte o valor que o computador criou:'))

computador = random.randint(0,5)

if chute == computador:
    print('Você venceu !! Você chutou {} eu pensei no número {}'.format(chute, computador))
else:
    print('Você errou! Eu pensei no número {} e você no número {}'.format(computador, chute))
print('------FIM------')
  

