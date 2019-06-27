alt = float(input('Altura da parede: '))
lar = float(input('Larguta da parede: '))
area = alt*lar

print('Sua parede tem a dimensão de {}x{} e sua área é de {}m2'.format(alt, lar, area))

tinta = area/2

print('Para pintar a área precisará de {} litros de tinta'.format(tinta))
