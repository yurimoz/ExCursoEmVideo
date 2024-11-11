numer = (int(input('Digite o primeiro numero: ')),
         int(input('Digite o segundo numero: ')),
         int(input('Digite o terceiro numero: ')),
         int(input('Digite o quarto numero: '))
         )

print(f'Os numero digitados foram: {numer}')
print(f'O numero 9 aparece {numer.count(9)} vezes')

if 3 in numer:
    print(f'O numero 3 aparece primeiro na {numer.index(3) + 1}ª posição')
else:
    print('O numero 3 não aparece entre os valores digitados')

print('Os numeros pares que aparecem na sequencia são: ')

for item in numer:

    if item % 2 == 0:
        print(item, end=' ')