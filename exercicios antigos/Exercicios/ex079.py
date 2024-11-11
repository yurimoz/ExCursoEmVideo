valores = []

while True:

    num = int(input('Digite um numero: '))

    if num not in valores:

        valores.append(num)
        print(f'O numero {num} foi adicionado')

    else:
        print(f'O valor {num} ja se encontra na lista, logo não foi adicionado')

    resp = str(input('Deseja inserir mais numeros[S/N]? ')).strip().upper()[0]

    while resp not in 'SN':
        print(f'Resposta invalida. Responda com "S" ou "N"')
        resp = str(input('Deseja inserir mais numeros[S/N]? ')).strip().upper()[0]

    if resp == 'N':
        break

valores.sort()
print(f'Os numeros adicionados foram: {valores}')