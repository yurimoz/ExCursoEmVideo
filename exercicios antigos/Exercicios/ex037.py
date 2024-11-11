x = int(input('Digite o numero que deseja converter: '))
base = int(input('''Para que base deseja converter
[1]BIN
[2]OCT
[3]HEX
'''))

if base == 1:
    print(f'{x} na base BIN é: {bin(x)[2:]}')

elif base == 2:
    print(f'{x} na base OCT é: {oct(x)[2:]}')

elif base == 3:
    print(f'{x} na base HEX é: {hex(x)[2:]}')

else:
    print(f'{base} não corresponde a nenhuma das alternativas. Tente novamente')