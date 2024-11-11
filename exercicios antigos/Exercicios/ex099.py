from time import sleep

def maior(*valor):
    if len(valor) == 0:
        mai = 0

    else:
        mai = valor[0]
        for v in valor:
            if v > mai:
                mai = v

    print('=-'*30)
    print('Analisando os valores passados...')
    print(f'Foram informados {len(valor)} valores ao todo')
    for v in valor:
        print(v, end=' ')
        sleep(0.5)
    print()
    print(f'O maior valor entre os digitados foi: {mai}')
    print('=-'*30)


maior(1.3, -4.8, -6, -1, 5.2, 11, 10.4, 16.6)
sleep(3)
maior(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
sleep(3)
maior(3, 23, 54, 7, 745, 34, 111, 345)
maior()