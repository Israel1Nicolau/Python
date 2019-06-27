sal = float(input('Quanto você ganha: R$ '))

if sal <= 1250:
    reajuste = (sal*0.15) + sal
else:
    reajuste = (sal*0.10) + sal
print('O seu salário atual é R${} e passará a ser R${}'.format(sal, reajuste))
