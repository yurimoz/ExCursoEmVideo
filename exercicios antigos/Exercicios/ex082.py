valores = []

while True:

    num = int(input('Digite um numero: '))

    resp = str(input('Deseja continuar[S/N]? ')).strip().upper()

    valores.append(num)

    while resp[0] not in 'SN':

        print('Resposta invalida! Tente novamente e responda com "S" ou "N"')
        resp = str(input('Deseja continuar[S/N]? ')).strip().upper()

    if resp[0] == 'N':
        break

pares = []
impares = []

for num in valores:

    if num % 2 == 0:
        pares.append(num)

    else:
        impares.append(num)

print(f'Os valores digitados foram: {valores}')


if len(pares) == 0:
    print('Não foi digitado nenhum valor par')
else:
    print(f'Os valores pares ditados: {pares}')


if len(impares) == 0:
    print('Não foi digitado nenhum valor impar')
else:
    print(f'Os valores impares ditados: {impares}')

