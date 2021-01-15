#desafio 31

dist = float(input('Digite a distancia da sua viagem para saber o valor: '))

vig1 = dist <= 200
vig2 = dist >= 201


if(vig1):
    pgv1 = dist * 0.50
    print('A sua viagem irá custar R$: {:.2f}'.format(pgv1))
else:
    pgv2 = dist * 0.45
    print('A sua viagem irá custar R$: {:.2f}'.format(pgv2))

print('------FIM------')