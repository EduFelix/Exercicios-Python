produto = float(input('Digite o valor do produto?'))
desconto = (produto * 5) / 100
preçof = produto - desconto

print('Seu produto custa Reais {},\nO desconto de 5% '
      'corresponde á Reais {:.2f},\n Você pagará pelo '
      'produto após o desconto o valor de Reais {:.2f}  '.format(produto, desconto, preçof))