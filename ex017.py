import math

oposto = float(input('Digite o valor do cateto oposto?'))
adjacente = float(input('Digite o valor do cateto adjacente?'))
hipo = math.hypot(oposto, adjacente)

print('A hipotenusa é {}'.format(hipo))
