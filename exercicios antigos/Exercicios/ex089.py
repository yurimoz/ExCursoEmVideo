alunos = []
aluno = []
notas = []

while True:
    aluno.append(str(input('Digite o nome do aluno: ')).strip().title())
    notas.append(float(input('Digite a 1ª nota: ')))
    notas.append(float(input('Digite a 2ª nota: ')))
    aluno.append(notas.copy())
    media = (notas[0] + notas[1]) / 2
    aluno.append(media)
    alunos.append(aluno.copy())
    notas.clear()
    aluno.clear()

    resp = str(input('Deseja continuar[S/N]? ')).strip().upper()

    while resp[0] not in 'SN':
        print('Entrada invalida. Tente novamente!')
        resp = str(input('Deseja continuar[S/N]? ')).strip().upper()

    if resp[0] == 'N':
        break

print('-='*20)
print('Nº.'.ljust(5), end='')
print('Nome'.ljust(20), end='')
print('Media'.rjust(5))
print('-'*30)

for num, pessoa in enumerate(alunos):

    print(f'{num:<5}', end='')
    print(f'{pessoa[0]:.<20}', end='')
    print(f'{pessoa[2]:>3.2f}')

flag = int(input('Digite a numero do aluno do qual quer ver as notas(Nª negativo para sair): '))

while flag >= 0:

    if flag > len(alunos) - 1:
        print(f'Aluno {flag} não cadastrado.')

    else:
        print(f'{alunos[flag][0]}.......{alunos[flag][1]}')

    flag = int(input('Digite a numero do aluno do qual quer ver as notas(Nª negativo para sair): '))
