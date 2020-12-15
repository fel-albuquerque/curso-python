#desafio-fase-004
val = input('Digite algo:  ')
print('O que voce digitou é {}:'.format(type(val)))
print('Só tem espaços?', val.isspace())
print('É um numero?', val.isalnum())
print('É alfabetico?', val.isalpha())
print('É maiuscula?', val.isupper())