#desafio 34

sal = float(input('Digite o seu salario para saber o seu aumento R$: '))

aumento1 = sal > 1250.00
aumento2 = sal < 1249.00

if(aumento1):
    aumento1 = (sal * 10) / 100 + sal
    print('Seu salario é {:.2f} \nCom o aumento seu salário é {:.2f}'.format(sal, aumento1))
else:
    aumento2 = (sal * 15) / 100 + sal
    print('Seu salario é {:.2f} \nCom o aumento seu salário é {:.2f}'.format(sal, aumento2))