from time import sleep
time = list()
jogador = dict()
gols = list()
while True:

    jogador.clear()
    gols.clear()
    jogador['nome'] = str(input('Digite o nome do jogador: ')).strip().title()
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    for i in range(0, jogador['partidas']):
        gols.append(int(input(f'Quantos gols {jogador["nome"]} fez na {i + 1}ª partida: ')))

    jogador['gols'] = gols.copy()

    jogador['total'] = sum(gols)

    time.append(jogador.copy())

    resp = str(input('Quer continuar[S/N]: ')).strip().upper()

    while resp not in 'SN':
        print('Entrada invalida! Responda com S ou N')
        resp = str(input('Quer continuar[S/N]: ')).strip().upper()

    if resp == 'N':
        break

print('~='*30)
print('='*40)
print('cod'.ljust(5), end='')
print('Nome'.ljust(15), end='')
print('Gols'.ljust(15), end='')
print('Total'.ljust(5))
print('-'*40)

for cod, pessoa in enumerate(time):
    print(f'{cod:<5}{pessoa["nome"]:<15}{str(pessoa["gols"]):<15}{pessoa["total"]:>5}')

print('-'*40)

while True:

    numjog = int(input('Digite o cod do jogador do qual deseja ver os dados(negativo para sair): '))

    if numjog < 0:
        print('finalizando...')
        break

    if numjog > len(time) - 1:
        print(f'O jogador {numjog} não foi cadastrado')

    else:
        print(f'LEVANTANDO DADOS DE {time[numjog]["nome"].upper()}')
        sleep(1)
        for p, g in enumerate(time[numjog]['gols']):
            print(f'No {p+1}º jogo fez {g} gols')
            sleep(1)

        print('='*15)
