dist = int(input('Qual a distância da viagem em Km/h: '))

if dist <= 200:
    preco = dist*0.50
else:
    preco = dist*0.45
print('A distância da viagem é de {} Km/h\n'
      'E o preço será de R${}'.format(dist, preco))

# preco = dist*0.50 if dist <= 200 else dist*0.45


