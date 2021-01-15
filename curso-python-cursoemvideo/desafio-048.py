#desafio-048

print('-='*4,'Multiplos de TRES','-='*4)

soma = 0 
cont = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        cont = cont + 1
        soma = soma + i
print ('A soma de todos os valores {} solicitados é {} '.format(cont, soma))
print('-='*10,'FIM', '-='*10)

