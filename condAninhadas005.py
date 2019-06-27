from datetime import date

ano_nasc = int(input('Digite seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc

print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Categoria mirim')
elif idade <= 14:
    print('Categoria infantil')
elif idade <= 19:
    print('Categoria junior')
elif idade <= 25:
    print('Categoria sênior')
else:
    print('Categoria master')

