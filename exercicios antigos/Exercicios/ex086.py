matriz = [[], [], []]

for i in range(0, 3):
    for j in range(0, 3):
        valor = int(input(f'Digite um valor para a linha {i + 1} coluna {j + 1}: '))
        matriz[i].append(valor)

for linha in matriz:
    for numero in linha:
        print(f'[{numero:^5}]', end='')
    print('')