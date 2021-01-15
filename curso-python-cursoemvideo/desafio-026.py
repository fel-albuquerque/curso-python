#desafio-026

frase = str(input('Digete uma frase: ')).upper().strip()
print('A Letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra apareceu na posição {}'.format(frase.find('A')+1))
print('A ultime vez que apareceu a letra A {}'.format(frase.rfind('A')+1))