#desafio 29

vel = float(input('Digite sua velocida no radar: '))

multa = vel >= 81 
nomulta = vel <=80
pgmulta = (vel - 80) * 7

if (multa):
    vel > 81 == multa 
    print('Você foi multado e o valor da sua multa é {:.2f}:'.format(pgmulta))
else:
    vel <= 80 == nomulta
    print('Voce nao foi multado !!! Siga sua viagem com segurança !!')

print('------FIM------')