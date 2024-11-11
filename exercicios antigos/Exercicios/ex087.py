matriz = [[], [], []]

print('Vamos construir uma matriz!')

for i in range(0, 3):
    for j in range(0, 3):
        num = int(input(f'Digite um numero para a linha {i + 1} coluna {j + 1}: '))
        matriz[i].append(num)

pares = 0
for linha in matriz:

    for valor in linha:

        if valor % 2 == 0:

            pares += valor


tercol = 0

for i in range(0, 3):

    tercol += matriz[i][2]

maiorseg = max(matriz[1])

for linha in matriz:
    for valor in linha:
        print(f'[{valor:^5}]', end='')
    print('')

print(f'A soma de todos os pares: {pares}')
print(f'A soma dos valores da terceira coluna: {tercol}')
print(f'O maior valor da segunda linha: {maiorseg}')