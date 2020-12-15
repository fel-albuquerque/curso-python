#desafio-008

val = float(input('Digite um valor em metros para saber em cm e mm: '))

cm = val * 100
mm = val * 1000

print('O valor digitado é {}, em centimetros é {}, e em milimetros {}: '.format(val,cm,mm))