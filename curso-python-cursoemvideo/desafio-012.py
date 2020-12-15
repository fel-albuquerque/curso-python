#desafio-012

val = float(input('Digite o valor do produto: R$ '))

prod = (val * 5) / 100
desc = val - prod 

print('Valor do produto é {} , com o desconto fica R$ {:.2f}'.format(val,desc))