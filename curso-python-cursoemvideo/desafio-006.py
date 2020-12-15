#desafio-006

num = int(input('Digite um número para saber o seu dobro, triplo e a raiz quadrada dele: '))

d = num *2
t = num *3
r = num ** (1/2)

print('O valor digitado é {} \nO seu dobro é {}, \nO triplo é {}, \nRaiz quadrada é {:0.3f} '.format(num,d,t,r))