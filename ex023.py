nun = int(input('Digite um numero que possua até quatro digitos?'))
u = nun // 1 % 10
d = nun // 10 % 10
c = nun // 100 % 10
m = nun // 1000 % 10
print('Unidades {}'.format(u))
print('Dezenas {}'.format(d))
print('Centenas {}'.format(c))
print('Milhar {}'.format(m))
