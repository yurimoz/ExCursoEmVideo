from random import randint
from time import sleep
from operator import itemgetter

jogo = dict()
jogo['jogador1'] = randint(1, 6)
jogo['jogador2'] = randint(1, 6)
jogo['jogador3'] = randint(1, 6)
jogo['jogador4'] = randint(1, 6)

#ranking = dict()

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('Que os jogos comecem!')

for k, v in jogo.items():
    sleep(1)
    print(f'{k} tirou {v} no dado')

sleep(2)

print('~='*30)
print('RANKING'.center(60))
print(('~='*30))

c=1


for k, v in ranking:
    sleep(1)
    print(f'{c}º LUGAR: {k} com {v}'.center(60))
    c += 1