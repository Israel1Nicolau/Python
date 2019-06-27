from math import sqrt, ceil, floor
import random

num = int(input('Digite um número: '))

raiz = sqrt(num)

print(floor(raiz))
print('='*50)

numTeste = random.random() #número float de 0 à 1
print(numTeste)

numTeste = random.randint(1, 15)
print(numTeste)


