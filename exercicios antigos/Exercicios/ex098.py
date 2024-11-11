from time import sleep

def contador(ini, fim, pas):
    
    if pas == 0:
        pas = 1

    print(f'Realizando contagem de {ini} a {fim} com passo {pas}')
    if fim > ini:

        for c in range(ini, fim + 1, pas):
            print(c)
            sleep(0.5)
    else:

        if pas > 0:
            for c in range(ini, fim - 1, -1 * pas):
                print(c)
                sleep(0.5)
        elif pas < 0:
            for c in range(ini, fim - 1, pas):
                print(c)
                sleep(0.5)


contador(1, 10, 1)
contador(10, 0, -2)
contador(int(input('Digite o inicio: ')), int(input('Digite o fim: ')), int(input('Digite o passo: ')))
