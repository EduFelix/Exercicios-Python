import random
from time import sleep
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
numero = int(input('Em que número eu pensei?'))
print('Processando...')
sleep(3)
nc = random.randrange(1,5)
print("você digitou {} eu pensei no número {}".format(numero, nc))
if(nc == numero):
    print('Acertou, Parabéns!')

else:
    print('Infelizmente você erro, tente outra vez.')


