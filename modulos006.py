from random import shuffle

p1 = str(input('Nome da pessoa: '))
p2 = str(input('Nome da pessoa: '))
p3 = str(input('Nome da pessoa: '))
p4 = str(input('Nome da pessoa: '))

lista = [p1, p2, p3, p4]
shuffle(lista)

print('A ordem de apresentação\n {}'.format(lista))
