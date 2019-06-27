dias = int(input('Quantos dias o carro ficou alugado? '))
km = float(input('Quantos km você andou com ele? '))
preco = (dias*60)+(km*0.15)

print('O carro foi alugado durante {}dia(s).\nAndou {}km.\nO custo do aluguel ficou em R${:.2f}'.format(dias, km, preco))
