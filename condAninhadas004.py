n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = round((n1+n2)/2)

print('Sua média foi {}'.format(media))
if media < 5:
    print('\033[31mReprovado!\033[m')
elif media >= 5 and media < 7:
    print('\033[33mRecuperação!\033[m')
elif media >= 7:
    print('\033[36mAprovado!\033[m')
