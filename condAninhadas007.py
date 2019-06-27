from random import randint
cores = {'limpa': '\033[m',
         'negrito': '\033[1m',
         'azul negrito': '\033[1;34m'}

print('{}{:=^40}'.format(cores['negrito'], 'LOJAS LOJAS'))
preco = randint(200, 250)

print('{}O preço do seu produto: R${}'.format(cores['azul negrito'],preco))
print('{}ESCOLHA A OPÇÃO DE PAGAMENTO:{}\n'
      '1 - à vista dinheiro/cheque: 10% de desconto\n'
      '2 - à vista no cartão: 5% de desconto\n'
      '3 - em até 2x no cartão: preço normal\n'
      '4 - 3x ou mais no cartão: 20% de juros\n'.format(cores['negrito'], cores['limpa']))
print('{}{:=^40}{}'.format(cores['negrito'], '', cores['limpa']))
opcao = int(input('Qual opção você prefere? '))

if opcao == 1:
    novo_preco = preco - (preco*0.10)
    print('O valor do produto é R${}\n'
          'E com os 10% de desconto ficará por R${}'.format(preco, novo_preco))
elif opcao == 2:
    novo_preco = preco - (preco*0.05)
    print('O valor do produto é R${}\n'
          'E com os 5% de desconto ficará por R${}'.format(preco, novo_preco))
elif opcao == 3:
    novo_preco = preco
    print('O valor do produto é R${}\n'
          'Com a opção escolhida, o valor final do produto será o mesmo.'.format(preco))
elif opcao == 4:
    novo_preco = preco + (preco*0.20)
    tot_parc = int(input('Quantas parcelas? '))
    if tot_parc < 3:
        print('Inválido. Tente novamente')
    else:
        parcela = novo_preco/tot_parc
        print('Sua compra será parcelada em {}x de R${:.2f} com juros'.format(tot_parc, parcela))
else:
    novo_preco = 0
    print('Opção inválida. Tente novamente')
