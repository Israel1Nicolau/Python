reta1 = float(input('Digite o valor do primeiro segmento: '))
reta2 = float(input('Digite o valor do segundo segmento: '))
reta3 = float(input('Digite o valor do terceiro segmento: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1+ reta2:
    print('Os segmentos formam um triângulo, ', end='')
    if reta1 == reta2 == reta3:
        print('este triângulo é equilátero')
    if reta1 != reta2 != reta3 != reta1:
        print('este triângulo é Escaleno')
    else:
        print('este triângulo é Isósceles')
else:
    print('Os segmentos não podem formar um triângulo')
