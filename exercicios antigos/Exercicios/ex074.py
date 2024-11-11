from random import randint

numer = (randint(0, 100),
         randint(0, 100),
         randint(0, 100),
         randint(0, 100),
         randint(0, 100))

print(f'Os numeros sorteados foram: {numer}')
print(f'O menor valor sorteado foi: {sorted(numer)[0]}')
print(f'O menor valor sorteado foi: {sorted(numer)[-1]}')
