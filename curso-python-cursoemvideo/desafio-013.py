#desafio-013

val = float(input('Digite o seu salario: R$'))

sal = (val * 15) / 100 + val
#nsal = val + sal 

print('O salario anterior era de {}  com aumento de 15 por cento foi para R$ {:.2f} '.format(val,sal))
