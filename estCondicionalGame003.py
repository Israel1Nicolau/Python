from random import randint
from time import sleep

print('-=-'*20)
print('JOGO DA ADIVINHAÇÃO')
print('-=-'*20)

eu = randint(0, 5) # sorteando um número

jogador = int(input('De 0 à 5, em que número estou pensando? \n'))
print('PROCESSANDO...')
sleep(3)

if jogador == eu:
    print('-'*30)
    print('O número que você escolheu foi {} e o que o eu pensei foi {}.\n'
          'Você venceu!'.format(jogador, eu))
    print('-'*30)
else:
    print('-'*30)
    print('O número que você escolheu foi {} e o que o eu pensei foi {}.\n'
          'Eu venci!'.format(jogador, eu))
    print('-'*30)
