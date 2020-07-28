km = int(input('Digite a velocidade do carro?'))
multa = (km - 80)*7
if(km > 80):
    print('Você foi multado')
    print('O valor da multa é R$: {:.2f}'.format(multa))