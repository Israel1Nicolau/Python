nome = str(input('Digite seu nome: ')).strip().capitalize()

if nome == 'Israel':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Nome bastante comum')
elif nome in 'Ana Juliana Elisabeth Joana':
    print('Belo nome feminino')
'''else:
    print('Nome normal!')'''
print('Prazer em te conhecer {}'.format(nome))
