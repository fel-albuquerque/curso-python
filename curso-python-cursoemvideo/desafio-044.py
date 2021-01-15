#desafio-044

produto = float(input('Digite o valor do produto R$  '))
print('''Digite a forma de pagamento:
[1]-Dinheiro/cheque 
[2]-A vista no cartao
[3]-Em 2 vezes no cartao
[4]-Em 3 vezes ou mais no cartao  ''')
opção = int(input('Qual é a opção ? '))
print('A forma de pagamento escolhida {}'.format(opção))

if opção == 1 :
    desconto = produto - (produto * 10 / 100)  
    print('O Valor da sua compra R$ {:.2f}, O Valor do desconto é R$ {:.2f}'.format(produto, desconto))
elif opção == 2 :
    desconto2 = produto - (produto * 5 / 100)
    print('O valor da sua compra R$ {:.2f}, seu desconto R$ {:.2f}'.format(produto, desconto2))
elif opção == 3:
    print('O Valor da sua compra R$ {:.2f} , por ser em duas vezes não há desconto!!'.format(produto))
elif opção == 4:
    acres = produto + (produto * 20 / 100)
    totparcela = int(input('Quantas parcelas? '))
    parcela = produto /totparcela
    print('O Valor da sua compra {:.2f}, numero de parcela {}x de parcela {} com o acrescimo R$ {:.2f}'.format(produto, totparcela, parcela, acres))
else:
    opção = produto
    print('Opção invalida para PAGAMENTO tente novamente !!!')
