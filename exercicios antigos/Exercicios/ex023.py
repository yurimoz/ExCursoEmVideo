numero = int(input('Digite um numero de 0 a 9999: '))
milhar = numero // 1000 % 10
centena = numero // 100 % 10
dezena = numero // 10 % 10
unidade = (numero % 10)
print(f'Milhar: {milhar}')
print(f'Centena: {centena}')
print(f'Dezena: {dezena}')
print(f'Unidade: {unidade}')
