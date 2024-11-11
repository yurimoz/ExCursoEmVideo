pessoas = list()
individuo = dict()
mulheres = list()
acimamedia = list()

while True:

    individuo['nome'] = str(input('Digite o nome: ')).strip().title()
    individuo['sexo'] = str(input('Digite o sexo[M/F]: ')).strip().upper()
    while individuo['sexo'] not in 'MF':
        print('Entrada invalida!')
        individuo['sexo'] = str(input('Digite o sexo[M/F]: ')).strip().upper()
    individuo['idade'] = int(input('Digite a idade: '))
    pessoas.append(individuo.copy())

    if individuo['sexo'] == 'F':
        mulheres.append(individuo.copy())

    resp = str(input('Quer continuar [S/N]: ')).strip().upper()

    while resp[0] not in 'SN':
        print('Entrada invalida')
        resp = str(input('Quer continuar [S/N]: ')).strip().upper()

    if resp[0] == 'N':
        break

totidade = 0
media = 0

for pessoa in pessoas:
    totidade += pessoa['idade']

media = totidade / len(pessoas)

for pessoa in pessoas:
    if pessoa['idade'] >= media:
        acimamedia.append(pessoa.copy())

print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'A media de idade do grupo é: {media:.2f}')
print('As mulheres do grupo:')

for mulher in mulheres:
    for k, v in mulher.items():
        print(f'{k} = {v}', end='   ')

print()

print(f'As pessoas com idade superior a media {media:.2f}:')

for pessoa in acimamedia:
    for k, v in pessoa.items():
        print(f'{k} = {v}', end='   ')

print()
print('FIM')
