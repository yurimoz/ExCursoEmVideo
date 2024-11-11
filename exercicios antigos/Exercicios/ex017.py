import math
ca = float(input('Comprimento do cateto adjacente: '))
co = float(input('Comprimento do cateto oposto: '))
hip = math.sqrt((pow(ca, 2) + pow(co, 2)))
print(f'A hipotenusa de um triangulo cujo os catetos são {ca} e {co} é: {hip:.2f}')
