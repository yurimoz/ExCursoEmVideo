numeros = []
pares = []
impares = []
numeros.append(pares)
numeros.append(impares)

for c in range(0, 7):
    num = int(input(f'Digite o {c + 1}º numero: '))

    if num % 2 == 0:
        pares.append(num)

    else:
        impares.append(num)

pares.sort()
numeros[1].sort()

print(f'Os valores pares digitados: {numeros[0]}')
print(f'Os valores impares digitados: {numeros[1]}')