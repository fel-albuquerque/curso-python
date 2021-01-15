#desafio-043

peso =   float(input('Digite o seu peso? (KG) '))
altura = float(input('Digite sua altura?(m) '))

imc = peso / (altura * altura)

if imc <= 18.5:
    print('Abaixo do peso !')
elif imc >= 18.5 and imc <= 25:
    print('Peso ideal !')
elif imc >= 25.1 and imc <= 30:
    print('Sobre peso')
elif imc >= 30.1 and imc <= 40:
    print('Você está Obesidade')
elif imc >= 40:
    print('Você esta com obesidade morbida')
    
