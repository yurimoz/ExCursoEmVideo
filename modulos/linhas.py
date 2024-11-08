def crialinha(tam, tipo='-'):

    print(tipo*tam)


def linhamenu(msg = '', tipo = '-', tam = 50):

    crialinha(tam, tipo)
    print(msg.center(tam))
    crialinha(tam, tipo)

