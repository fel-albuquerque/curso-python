#desafio-041

import datetime

nascimento = int(input('Digite o ano do seu nascimento: '))

ano = datetime.date.today().year 

idade = ano - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade >= 21:
    print('Você faz parte da categoria Master! Pois sua idade é {}'.format(idade))
elif idade >= 20:
    print('Sua idade é {} , portanto você é da categoria SENIOR'.format(idade))
elif idade <= 15 and idade >= 19:
    print('Sua idade é {}, portanto você é da categoria JUNIOR'.format(idade))
elif idade >= 10 and idade >=14 :
    print('Sua idade é {}, portanto você é da categoria Infantil'.format(idade))
elif idade <= 9:
    print('Sua idade é {}, portanto você é da categoria MIRIM'.format(idade))
else:
    print('Você é MATER !!')
