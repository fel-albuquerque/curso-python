#desafio-027

nome = str(input('Digete o seu nome completo: ')).strip()
nome = nome.split()
print('Muito prazer em lhe conhecer')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {} '.format(nome[len(nome)-1]))