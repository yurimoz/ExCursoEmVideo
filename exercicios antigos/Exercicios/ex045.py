from random import choice
from time import sleep

maos = ['Pedra', 'Papel', 'Tesoura']
pc = choice(maos)
print('Vamos jogar jokenpo!')

jogador = int(input('Escolha sua mão:\n'
                    '[0] Pedra\n'
                    '[1] Papel\n'
                    '[2] Tesoura\n'))

print('Vamos revelar no já')
sleep(1)
print('1... 2... 3...')
sleep(1)
print('JÁ!!')
sleep(1)

jogador = maos[jogador]

print(f'Voce: {jogador}')
print(f'PC: {pc}')

sleep(3)

pcwins = False


if jogador == 'Pedra':

    if pc == 'Papel':
        pcwins = True

elif jogador == 'Papel':

    if pc == 'Tesoura':
        pcwins = True

elif jogador == 'Tesoura':

    if pc == 'Pedra':
        pcwins = True


if jogador == pc:
    print('Parece que empatamos dessa vez! Vamos denovo?')

elif pcwins is False:
    print(f'{jogador} ganha de {pc}! Você me venceu!')

elif pcwins:
    print(f'{pc} ganha de {jogador}! Eu venci!')