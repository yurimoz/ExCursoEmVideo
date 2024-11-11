def leiaDinheiro(msg=''):
    valor = str(input(f'{msg}')).strip()

    while valor.isnumeric() is False:
        dinheiro = False

        if '.' in valor:
            if valor.count('.') == 1 and len(valor)>1:
                for v in valor:
                    if v.isnumeric() or v == '.':
                        dinheiro = True
                    else:
                        dinheiro = False
                        break

        if dinheiro:
            break
        print(f'ENTRADA INVALIDA! {valor} não é um numero!')
        valor = str(input(f'{msg}')).strip()

    valor = float(valor)

    return valor

