km = float(input('Quantos kilomentros percorridos?'))
dias = float(input('Por quantos dias o carro foi alugado?'))
vTotal = (60*dias)+ (0.15*km)
print('O preço a pagar pelo o aluguel do carro durante {} dias'
      'pecorrendo {} kilomentros. Corresponde a Reais {}'.format(dias, km, vTotal))