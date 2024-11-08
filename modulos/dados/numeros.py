from modulos import cores


def leiaInt(msg=''):


    while True:

        try:
            valor = input(msg).strip()
            valor = int(valor)
            break



        except KeyboardInterrupt:
            valor = 0
            print(cores.roxo('\nO usuario decidiu não digitar um numero inteiro'))
            break


        except:
            print(cores.vermelho(f'ENTRADA INVALIDA! por favor digite um numero inteiro'))
            continue

    return valor


def leiaFloat(msg=''):
    flt = False

    while flt is False:

        try:
            valor = input(msg).strip()
            valor = float(valor)
            flt = True


        except KeyboardInterrupt:
            valor = 0
            print(cores.roxo('\nO usuario decidiu não digitar um numero real'))
            flt = True


        except:
            print(cores.vermelho(f'ENTRADA INVALIDA! por favor digite um numero real'))

    return valor