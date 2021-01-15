#desafio-049

print('-=-'*5,'TABUADA','-=-'*5)

num = int(input('Digite um número para ver sua tabuada: '))
print('TABUA DO {}'.format(num))
for i in range (0,11,):
    multi = num * i 
    print('{} x {} = {}'.format(num, i, multi))
print('FIM')


#OUTRA FORMA

''' num = int(input('Digite um número para ver sua tabuada: '))
    for c in range(1, 11)
        print('{} x {:2} = {} '.format(num, c, c*num))'''