sal = float(input('Qual é o seu salario em R$?'))
if sal >1250:
    ajuste = (sal*10)/100
    print('Seu novo salário em R$ é: {}'.format(sal+ajuste))
else:
    ajuste = (sal*15)/100
    print('Seu novo salário em R$ é: {}'.format(sal+ajuste))
