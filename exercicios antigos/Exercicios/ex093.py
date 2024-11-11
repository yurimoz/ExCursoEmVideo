jogador = dict()
gols = list()
total = 0
jogador['nome'] = str(input('Digite o nome do jogador: ')).strip().title()
jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
jogador['gols'] = gols

for i in range(0, jogador['partidas']):

     gol = int(input(f'Quantos gols o jogador fez na {i+1}ª partida: '))
     gols.append(gol)
     total += gol

jogador['total'] = total

print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]}.')
for partida, gol in enumerate(jogador['gols']):
    print(f'Na {partida + 1}ª partida {jogador["nome"]} fez {gol} gols.')
print(f'Total: {jogador["total"]}')





