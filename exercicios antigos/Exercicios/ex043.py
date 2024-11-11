peso = float(input('Digite seu peso(kg): '))
altura = float(input('Digite sua altura(m): '))
imc = peso / (altura ** 2)

print(f'Seu IMC é: {imc:.1f}')

if imc < 18.5:
    print('ABAIXO DO PESO')

elif imc < 25:
    print('PESO IDEAL')

elif imc < 30:
    print('SOBREPESO')

elif imc < 40:
    print('OBESIDADE')

else:
    print('OBESIDADE MORBIDA')
