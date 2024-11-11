def dobro(valor = 0, form = True):
    valor *= 2

    if form:
        return f'R${valor:.2f}'
    else:
        return valor


def metade(valor, form = True):
    valor /= 2

    if form:
        return f'R${valor:.2f}'
    else:
        return valor


def aumentar(valor, por, form=True):

    valor = valor + valor * (por / 100)

    if form:
        return f'R${valor:.2f}'
    else:
        return valor


def diminuir(valor, por, form=True):

    valor -= valor * (por / 100)

    if form:
        return f'R${valor:.2f}'
    else:
        return valor


def resumo(p, pa, pd):
    print('-'*40)
    print('RESUMO DO VALOR'.center(40))
    print('-'*40)
    print('Preço analizado'.ljust(30, '.'), end='')
    print(f'R${p:.2f}'.rjust(10, '.'))
    print('Dobro do preço'.ljust(30, '.'), end='')
    print(dobro(p).rjust(10, '.'))
    print('Metade do preço'.ljust(30, '.'), end='')
    print(metade(p).rjust(10, '.'))
    print(f'{pa}% de aumento'.ljust(30, '.'), end='')
    print(aumentar(p, pa).rjust(10, '.'))
    print(f'{pd}% de redução'.ljust(30, '.'), end='')
    print(diminuir(p, pd).rjust(10, '.'))
    print('-'*40)