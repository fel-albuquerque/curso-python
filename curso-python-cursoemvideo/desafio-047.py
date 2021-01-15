#desafio-047

print('=='*4,'NUMEROS PARES','=='*4)
for i in range(1,50):
    resto = i % 2
    if resto == 0:
        print(i, end=' ')
print('FIM')

#SEGUNDA FORMA VISTA EM AULA
''' for n in range(2, 51, 2):
        print(n, end=' ')
    print('FIM')'''