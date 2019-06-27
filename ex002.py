n = input('Digite algo: ')

print(type(n))

print(n.isnumeric()) # se pode-se converter para número
print(n.isalpha()) # alpha é para alfabeto
print(n.isalnum()) # alfabeto e número
print(n.isupper()) # se está com todas as letras maiúsculas
print(n.isdecimal()) # se pode-se converter para número
print(n.istitle()) # se está capitalizada

print('é númerico? {}, é alfabético? {}, é alfanumérico? {}, é tudo em letras maiúscula? {}, é decimal? {}, é capitalizado? {}'
      .format(n.isnumeric(), n.isalpha(), n.isalnum(), n.isupper(), n.isdecimal(), n.istitle()))
