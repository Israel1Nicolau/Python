n1 = int(input('Primeira nota: '))
n2 = int(input('Segunda nota: '))
m = (n1+n2)/2

print('A nota 1 do aluno foi: {}\nA nota 2 foi: {}\ne a média é: {:.0f}'.format(n1, n2, m))

print('======================================')

metro = float(input('Quantos metros para conversão? '))
centi = metro*100;
mili = metro*1000;

print('{} metro(s) são {} centimetros e {} milimetros'.format(metro, centi, mili))
