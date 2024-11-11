numeros = []

for i in range(0, 5):
    num = int(input(f'Digite o {i + 1}º numero: '))

    if i == 0:
        numeros.append(num)
        print(f'O numero {num} foi adicionado na posição 0 da lista')

    elif i == 1:
        if num > numeros[0]:
            numeros.append(num)
            print(f'O numero {num} foi adicionado no final da lista')

        else:
            numeros.insert(0, num)
            print(f'O numero {num} foi adicionado na posição 0 da lista')

    else:
        for j in range(0, i):

            if num <= numeros[j]:
                numeros.insert(j, num)
                print(f'O numero {num} foi adicionado na posição {j} da lista')
                break

            if num >= numeros[-1]:
                numeros.append(num)
                print(f'O numero {num} foi adicionado no final da lista')
                break


print(numeros)

