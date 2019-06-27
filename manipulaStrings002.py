nome = str(input('Digite seu nome: ')).strip()

print('Nome maiúsculo: {} '.format(nome.upper()))
print('Nome minúsculo: {} '.format(nome.lower()))
print('Nome capitalizado: {} '.format(nome.capitalize()))
print('Nome titulado: {} '.format(nome.title()))

print('Tamanho do nome: {} '.format(len(nome)))
print('Tamanho do nome sem espaços: {} '.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

separa = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))













