#desafio-052

print('-=-'*5,'NUMEROS PRIMOS','-=-'*5)

num = int(input('Digite um número inteiro: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        tot += 1
print('O número {} foi divisivel {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso ele É PRIMO')
else:
    print('E por isso ele NAO É PRIMO !!')
print('FIM')

