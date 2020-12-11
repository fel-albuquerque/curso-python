idade_str = input("Digite sua idade: ")
idade = int(idade_str)

if (idade > 18):
    print("Voce é maior de idade")
else:
    if (idade < 12):
        print("Voce é uma criança")
    elif (idade > 12):
        print("Você é um adolescente")
