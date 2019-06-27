peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso/(altura*altura)
print('Seu IMC é {:.2f}'.format(imc))

if imc < 18.5:
    print('Está abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal')
elif imc >= 25 and imc < 30:
    print('Está com sobrepeso')
elif imc >= 30 and imc < 40:
    print('Obeso')
else:
    print('Obeso mórbido')

