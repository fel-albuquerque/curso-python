#desafio-040

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

med = (nota1 + nota2) / 2

if med >  7:
    print('Você foi Aprovado PARABENS! ')
elif med < 5:
    print('Você está REPROVADO ! ')
else:
    med >= 5.1 or med >= 6.9
    print('Você está de RECUPERACAO!!!')