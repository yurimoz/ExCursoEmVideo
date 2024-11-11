def fatorial(x=1, show=False):
    '''
    --> Calcula o fatorial de um numero
    :param x: O numero a ser calculado
    :param show: Mostrar ou não a conta
    :return: o fatorial do numero x
    '''
    f = 1
    for i in range(x, 0, -1):
        f *= i

    if show:
        resp = f'{x}! = '
        for i in range(x , 0, -1):
            if i == 1:
                resp += f'{i} = {f}'
            else:
                resp += f'{i} * '


    else:

        resp = f'{x}! = {f}'

    return resp

print(fatorial(6, show=True))
help(fatorial)