n = int(input('Digite um número para conversão: '))

print('--- ESCOLHA UMA OPÇÃO---\n'
            '[1]  Binário\n'
            '[2]  Octal\n'
            '[3]  Hexadecimal\n')
opcao = int(input('Opção escolhida: '))

if opcao == 1:
    print('{} convertido em binário é igual a {}'.format(n, bin(n)[2:]))
elif opcao == 2:
    print('{} convertido em octal é igual a {}'.format(n, oct(n)[2:]))
elif opcao == 3:
    print('{} convertido em hexa é igual a {}'.format(n, hex(n)[2:]))
else:
    print('Opção inválida')
