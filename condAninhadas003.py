from datetime import date

ano_nasc = int(input('Digite o ano que você nasceu: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc
atraso = idade - 18
falta = int(abs(atraso))

if idade < 18:
    ano_certo = ano_atual + falta
    print('Ainda não chegou a hora de se alistar!\n'
          'Você tem {} anos, seu alistamento é em {}.\n'
          'faltam {} ano(s)'.format(idade, ano_certo, falta))
elif idade == 18:
    print('Você tem {} anos. Essa é a hora de servir seu país!'.format(idade))
elif idade > 18:
    ano_certo = ano_atual - atraso
    print('Sua idade é {} anos!\n'
          'Você está {} ano(s) atrasado!\n'
          'Seu alistamento deveria ter sido em {}\n'
          'Se apresente imediatamente!'.format(idade, atraso, ano_certo))
