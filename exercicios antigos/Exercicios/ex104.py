def leiaint(msg = ''):
    num = input(msg).strip()

    if num.isnumeric():

        return (num)

    else:
        while num.isnumeric() is False:
            print(f'ERRO! "{num}" não é um numero inteiro')
            num = input(msg).strip()

        return num

n = leiaint('Digite um numero: ')
print(f'Você digitou o numero {n}')