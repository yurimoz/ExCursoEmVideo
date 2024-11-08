fundos = {'branco' : 40,
         'vermelho' : 41,
         'verde' : 42,
         'amarelo': 43,
         'azul' : 44,
         'roxo' : 45,
         'ciano' : 46,
         'cinza' : 47}


def azul(msg = '', estilo = 0, fundo = 0):

    if fundo == 0:
        texto = f'\033[{estilo};34m{msg}\033[m'
    else:
        texto = f'\033[{estilo};34;{fundos[fundo]}m{msg}\033[m'

    return texto


def vermelho(msg = '', estilo = 0, fundo = 0):

    if fundo == 0:
        texto = f'\033[{estilo};31m{msg}\033[m'
    else:
        texto = f'\033[{estilo};31;{fundos[fundo]}m{msg}\033[m'

    return texto


def verde(msg = '', estilo = 0, fundo = 0):

    if fundo == 0:
            texto = f'\033[{estilo};32m{msg}\033[m'
    else:
        texto = f'\033[{estilo};32;{fundos[fundo]}m{msg}\033[m'

    return texto


def amarelo(msg = '', estilo = 0, fundo = 0):

    if fundo == 0:
        texto = f'\033[{estilo};33m{msg}\033[m'
    else:
        texto = f'\033[{estilo};33;{fundos[fundo]}m{msg}\033[m'

    return texto


def roxo(msg = '', estilo = 0, fundo = 0):
    if fundo == 0:
        texto = f'\033[{estilo};35m{msg}\033[m'
    else:
        texto = f'\033[{estilo};35;{fundos[fundo]}m{msg}\033[m'

    return texto


def ciano(msg = '', estilo = 0, fundo = 0):
    if fundo == 0:
        texto = f'\033[{estilo};36m{msg}\033[m'
    else:
        texto = f'\033[{estilo};36;{fundos[fundo]}m{msg}\033[m'

    return texto

def cinza(msg = '', estilo = 0, fundo = 0):
    if fundo == 0:
        texto = f'\033[{estilo};37m{msg}\033[m'
    else:
        texto = f'\033[{estilo};37;{fundos[fundo]}m{msg}\033[m'

    return texto


def branco(msg = ''):

    texto = f'\033[m{msg}'

    return texto


def limpar():

    print('\033[m', end='')
