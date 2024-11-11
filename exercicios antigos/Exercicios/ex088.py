from random import randint
from time import sleep

print('~='*20)
print('MEGA-SENA'.center(40))
print('~='*20)


quant = int(input('Quantos jogos voce quer que eu sorteie?\n'))
jogos = []
sorteados = []
for c in range(0, quant):
    contador = 0
    while contador < 6:
        num = randint(1, 60)
        if num not in sorteados:
            sorteados.append(num)
            contador += 1
    sorteados.sort()
    jogos.append(sorteados.copy())
    sorteados.clear()

for numero, jogo in enumerate(jogos):
    sleep(1)
    print(f'Jogo {numero + 1}: {jogo}')