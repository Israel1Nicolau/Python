preco = float(input('Qual o valor do produto: '))
desc = (preco*0.05)
nPreco = preco-desc

print('O preço atual é {:.2f}\ncom o desconto de 5% ficará {:.2f}'.format(preco, nPreco))

print('='*40)

salFunc = float(input('Salário atual: '))
novoSal = salFunc*1.15

print('O salário do funcionário é de {:.2f}\n'
      'passará para {:.2f} com o reajuste de 15%'.format(salFunc, novoSal))
