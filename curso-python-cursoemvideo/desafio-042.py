#desafio-042

r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima PODEM FORMAR UM TRIANGO!', end='')
    if r1 == r2 == r3:
        print('Forma o triangulo EQUILATERO')
    elif r1 != r2 != r3 != r1:
        print('Forma o triangulo ESCALENO')
    else:
        print('Forma o triangulo ISOSCELES')
else:
    print('Os seguintemos acima NÃO PODEM formar um triangulo:')