salario = float(input('Digite o valor do salário?'))
ajuste = (salario*15)/100
salarioN = salario + ajuste
print('Você ganhava Reais{}, \n'
      'Teve um aumento salárial no valor de Reais {}\n'
      'Seu novo salário é Reais {}'.format(salario, ajuste, salarioN))