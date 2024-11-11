from random import randint
from time import sleep

def sorteia(lst):

    while True:
        if len(lst) == 5:
            break
        print(f'Sorteando o {len(lst) + 1}º numero...')
        sleep(1)
        num = randint(1, 100)
        print(f'{num}!')
        if num not in lst:
            print(f'O numero {num} foi adicionado a lista')
            lst.append(num)
            sleep(1)
        else:
            print(f'O numero {num} ja estava na lista portanto não foi adicionado')
            sleep(1)


def somaPar(lst):
    soma = 0
    print('Os valores pares adicionados: ', end='')
    for v in lst:
        if v % 2 == 0:
            sleep(0.5)
            print(v, end=' ')
            soma += v

    sleep(1)
    print()
    print(f'A soma entre eles é: {soma}')


numeros = list()
sorteia(numeros)
somaPar(numeros)


