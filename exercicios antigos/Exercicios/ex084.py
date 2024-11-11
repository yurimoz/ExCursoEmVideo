pessoas = []
pesadas = []
leves = []
ind = []

while True:

    ind.append(str(input('Digite o nome da pessoa: ')).strip().title())
    ind.append(int(input('Digite o peso da pessoa: ')))
    pessoas.append(ind.copy())

    if len(pesadas) == 0 or ind[1] == pesadas[0][1]:

        pesadas.append(ind.copy())

    else:

        if ind[1] > pesadas[0][1]:

            pesadas.clear()
            pesadas.append(ind.copy())

    if len(leves) == 0 or ind[1] == leves[0][1]:

        leves.append(ind.copy())

    else:

        if ind[1] < leves[0][1]:
            leves.clear()
            leves.append(ind.copy())

    ind.clear()

    resp = str(input('Quer cadastrar mais pessoas[S/N]? ')).strip().upper()

    while resp[0] not in 'SN':
        print('Opção invalida! Tente Novamente')
        resp = str(input('Quer cadastrar mais pessoas[S/N]? ')).strip().upper()

    if resp[0] == 'N':
        break

print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'Os mais pesados, com {pesadas[0][1]}kg, são: ', end='')

for p in pesadas:
    print(p[0], end=' ')

print(f'\nOs mais leves, com {leves[0][1]}kg, são: ', end='')

for l in leves:
    print(l[0], end=' ')
