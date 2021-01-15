#desafio 33

n1 = int(input('Digite um número jogador1: '))
n2 = int(input('Digite um número jogador2: '))
n3 = int(input('Digite um número jogador3: '))
#verifica o menor
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print('O menor valor digitado foi {}  \no maior digitado foi {} '.format(menor, maior))
