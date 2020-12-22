#desafio-023

num = int(input('Informe um numero: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando seu número ...')
print('Unidade é {}'.format(u))
print('Dezena é {}'.format(c))
print('Centena é {}'.format(d))
print('Milhar é {}'.format(m))