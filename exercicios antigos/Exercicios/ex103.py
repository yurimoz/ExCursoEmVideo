def ficha(nome='<desconhecido>', gols = 0):

    resp = f'O jogador {nome} fez {gols} gol(s) no campeonato.'

    return resp


jogador = str(input('Digite o nome do jogador: ')).strip().title()
goles = str(input('Digite o numero de gols: ')).strip()

if goles.isnumeric() is False:
    goles = 0

goles = int(goles)

if jogador == '':
    j = ficha(gols=goles)

else:
    j = ficha(jogador, goles)

print(j)
