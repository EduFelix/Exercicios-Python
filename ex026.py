frase = str(input('Digite uma frase?')).strip()
print('A letra A Aparece {}'.format(frase.upper().count('A')))
print('A primeira vez que a letra A aparece está na posição {}'.format(frase.upper().find('A')))
print('A ultima letra A aparece na posição {}'.format(frase.upper().rfind('A')))
