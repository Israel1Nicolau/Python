n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2

print('A sua média foi {}'.format(media))

if media <= 5:
    print('Dp seu lixo')
elif (media > 5) and (media < 7):
    print('Exame')
else:
    print('Parabéns passou')
