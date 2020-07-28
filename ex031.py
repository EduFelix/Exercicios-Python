nkm = int(input('Quantos kilomentros a distancia da viagem?'))
if nkm <=200:
    vpassagem = nkm *0.50
    print('O valor da passagem custará R$: {:.2f}'.format(vpassagem))
else:
    vpassagem = nkm * 0.45
    print('O valor da passagem custará R$: {:.2f}'.format(vpassagem))
