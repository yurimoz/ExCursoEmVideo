nota1 = float(input('Qual foi a sua primeira nota: '))
nota2 = float(input('Qual foi a sua segunda nota: '))
media = (nota1 + nota2) / 2

print(f'Sua média foi {media:.2f}')

if media >= 7:
    print('APROVADO!!')

elif media < 5:
    print('REPROVADO!!')

else:
    print('RECUPERAÇÃO')
