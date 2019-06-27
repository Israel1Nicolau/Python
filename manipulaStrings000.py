frase = '  Rafa é um lixo, de fato ele é  '

print(frase[0:4])
print(frase[0:8:2])
print(frase[:10])
print(frase[15:])
print(frase[10::2])

print(len(frase)) #tamanho da frase
print(frase.count('e'), frase.count('é')) #quantas vezes aparece
print(frase.count('0', 0, 14))
print(frase.find('fat')) #indica a PRIMEIRA posição do que foi procurado
print(frase.find('Welcome')) # retorna -1 indicando que não foi encontrado


print('Rafa' in frase) #retorna valor booleano indicando se existe ou não
print(frase.replace('Rafa', 'Everton Felipe')) #função replace
print(frase.upper())
print(frase.lower())
print(frase.capitalize()) #tudo minúsculo e a primeira em maiúsculo
print(frase.title()) #capitalize com todas as palavras
print(frase.strip()) #retira espaços inúteis
print(frase.rstrip()) #remove espaços da direita
print(frase.lstrip()) #remove espaços da esquerda

print(frase.split())
print(frase.split(','))
print('/'.join(frase))










