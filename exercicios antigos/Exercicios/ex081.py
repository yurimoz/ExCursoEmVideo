valores = []

while True:
    n = int(input('Digite um numero: '))
    valores.append(n)

    resp = str(input('Quer digitar outro?[S/N] ')).strip().upper()

    if resp[0] == 'N':
        break

valores.sort(reverse=True)

print(f'Foram digitados {len(valores)} numeros')
print('Os numeros digitados em forma decrescente:')
print(valores)

if 5 in valores:
    print('O numero 5 esta na lista')

else:
    print('O numero 5 não esta na lista')


