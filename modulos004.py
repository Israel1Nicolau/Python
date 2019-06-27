import math

angulo = float(input('Digite o ângulo que você deseja: '))

seno = math.sin(math.radians(angulo))
print('O ângulo de {} graus tem o seno de {:.2f}'.format(angulo, seno))

cos = math.cos(math.radians(angulo))
print('O ângulo de {} graus tem o cosseno de {:.2f}'.format(angulo, cos))

tan = math.tan(math.radians(angulo))
print('O ângulo de {} graus tem a tangente de {:.2f}'.format(angulo, tan))


