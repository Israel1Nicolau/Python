print(3**5)
print(8*(5-4)**8/4)
print(18%3)
print(pow(4,3))
print(81**(1/2)) # raíz de 81
print(127**(1/3)) # raíz cúbica
print('='*20)
print('Olá'*10)

nome = str(input('Qual é seu nome? '))
print('Prazer em te conhecer {:>10}!'.format(nome)) #alinhar à direita
print('Prazer em te conhecer {:^10}!'.format(nome)) #centralizar
print('Prazer em te conhecer {:=^30}!'.format(nome)) #centralizar e colocar símbolo de igual

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))

print('A soma vale {}'.format(n1+n2))


