r1 = float(input('Tamanho do primeiro segmento: '))
r2 = float(input('Tamanho do segundo segmento: '))
r3 = float(input('Tamanho do terceiro segmento: '))

lados = [r1, r2, r3]

if r1 >= (r2 + r3) or r2 >= (r1 + r3) or r3 >= (r1 + r2):
    print(f'{lados} não formam um triangulo!')

else:
    if r1 == r2 == r3:
        tipo = 'equilatero'

    elif r1 == r2 or r1 == r3 or r2 == r3:
        tipo = 'isóceles'

    else:
        tipo = 'escaleno'

    print(f'{lados} formam um trinagulo {tipo}!')
