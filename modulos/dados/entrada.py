from modulos import cores

def entradaint(msg = '', liminf = 1, limsup = 3):

    while True:
        try:
            n = input(cores.roxo(msg)).strip()
            n = int(n)

        except KeyboardInterrupt:

            print(cores.vermelho('Tem certeza que deseja interromper o programa? Aperte novamente para sair'))
            continue

        except:
            print(cores.vermelho('ENTRADA INVALIDA! FOR FAVOR DIGITE UM NUMERO INTEIRO'))
            continue

        if n > limsup or n < liminf:
            print(cores.amarelo(f'{n} não é uma opção valida no menu. Tente novamente'))

        else:
            return n
