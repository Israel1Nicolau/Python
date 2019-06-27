import emoji

veloc = float(input('Digite a velocidade em Km/h que o carro está: '))

vMulta = (veloc - 80)*7

if veloc > 80:
    print('Você será multado!\n'
          'Valor da multa R${:.2f}'.format(vMulta), emoji.emojize(':rage:', use_aliases=True))
print('Tenha um bom dia!')





