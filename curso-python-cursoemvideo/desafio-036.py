#desafio 036

casa = float(input('Qual o valor do imovel? '))
salario = float(input('Qual o valor do seu salario? '))
ano = int(input('Em quantos anos pretende pagar? '))
prestação =  casa / (ano * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, ano), end='')
print('  A prestação sera de R${:.2f}'.format(prestação))
if prestação <= minimo:
    print('Emprestimo LIBERADO')
else:
    print('Emprestimo NEGADO')