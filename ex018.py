import math
angulo = float(input('Digite o valor do ângulo?'))
seno = math.sin(math.radians(angulo))
coss = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print('O seno de {} é {}, o Cosseno de {} é{} e a tangente de {} é {}'.format(angulo, seno, angulo, coss, angulo, tan))