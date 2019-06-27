from random import randint

cores = {'limpa': '\033[m',
         'negrito': '\033[1m',
         'azul negrito': '\033[1;34m',
         'verde negrito': '\033[1;32m',
         'vermelho negrito': '\033[1;31m'}

print('{}-='.format(cores['negrito'])*10, 'PREÇO NORMAL DO PRODUTO', '-='*10, '{}'.format(cores['limpa']))
preco = randint(200, 250)

print(' '*25, '{}R${}{}'.format(cores['azul negrito'], preco, cores['limpa']), ' '*25)
print('{}ESCOLHA A OPÇÃO DE PAGAMENTO:{}\n'
      '1 - à vista dinheiro/cheque: 10% de desconto\n'
      '2 - à vista no cartão: 5% de desconto\n'
      '3 - em até 2x no cartão: preço normal\n'
      '4 - 3x ou mais no cartão: 20% de juros'.format(cores['negrito'], cores['limpa']))
print('{}-='.format(cores['negrito'])*20, '{}'.format(cores['limpa']))

opcao = int(input('Qual opção você prefere? '))

if opcao == 1:
    novo_preco = preco - (preco*0.10)
elif opcao == 2:
    novo_preco = preco - (preco*0.05)
elif opcao == 3:
    novo_preco = preco
else:
    novo_preco = preco + (preco*0.20)

print('{}-='.format(cores['negrito'])*20, '{}'.format(cores['limpa']))
print('A opcao de pagamento foi de número {}{}{}\n'
      'O valor do produto é {}R${}{}\n'
      'E com a opção de pagamento ficará por {}R${}{}'.format(cores['negrito'], opcao, cores['limpa'], cores['verde negrito'], preco, cores['limpa'], cores['vermelho negrito'] ,novo_preco, cores['limpa']))
print('{}-='.format(cores['negrito'])*20, '{}'.format(cores['limpa']))

