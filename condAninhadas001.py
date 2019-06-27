valor_casa = float(input('Digite o valor da casa: R$ '))
sal = float(input('Digite seu salario: R$'))
anos_pagar = int(input('Digite em quantos anos você pretende pagar: '))
parcela = valor_casa/(anos_pagar*12)

print('A casa custa R${:.2f}. O valor da parcela será R${:.2f}'.format(valor_casa, parcela))
if parcela > (sal*0.30):
    print('Não poderá comprar a casa. A parcela compromete 30% do salário!')
else:
    print('Legal pode pedir o empréstimo!')
