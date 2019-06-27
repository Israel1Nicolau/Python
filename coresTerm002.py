nome = 'Israel'

cores = {'limpa':'\033[m',
         'negritoVerm':'\033[1;31m',
         'verdeSubl':'\033[4;32m',
         'inverte':'\033[7;30;44m'}

print('Prazer, {}{}{}'.format(cores['negritoVerm'], nome, cores['limpa']))
print('Prazer, {}{}{}'.format(cores['inverte'], nome, cores['limpa']))
print('Prazer, {}{}{}'.format(cores['verdeSubl'], nome, cores['limpa']))
