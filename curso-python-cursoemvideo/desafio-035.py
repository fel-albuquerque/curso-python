#desafio 35
print('-='*20)
print('Analisador de Triangulos')
print('-='*20)
r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima PODEM FORMAR UM TRIANGO!')
else:
    print('Os seguintemos acima NÃO PODEM formar um triangulo:')
