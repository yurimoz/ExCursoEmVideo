valor = float(input('Digite o valor do produto: $'))
formadepgto = int(input('Escolha a forma de pagamento\n'
                        '[0] A vista no dinheiro/cheque (10% de desconto)\n'
                        '[1] A vista no cartão (5% de desconto)\n'
                        '[2] 2x no cartão (preço normal)\n'
                        '[3] 3x ou mais (20% de juros)\n'))

if formadepgto == 0:
    print('Você escolheu a vista no dinheiro/cheque!')
    print(f'O seu total é ${valor * 0.9: .2f}')

elif formadepgto == 1:
    print('Você escolheu a vista no cartão!')
    print(f'O seu total é ${valor * 0.95: .2f}')

elif formadepgto == 2:
    print('Você escolheu em parcelar 2x no cartão!')
    print(f'O seu total é ${valor} em duas parcelas de ${valor / 2:.2f}')

elif formadepgto == 3:
    print('Você escolheu parcelar em 3x ou mais!')
    parcelas = int(input('Em quantas vezes você quer parcelar?\n'
                         '[3] 3x\n'
                         '[4] 4x\n'
                         '[5] 5x\n'
                         '[6] 6x\n'))
    valorjuros = valor * 1.2
    if parcelas == 3:
        print(f'O seu total é ${valorjuros} em 3 parcelas de ${valorjuros/3:.2f}')
    elif parcelas == 4:
        print(f'O seu total é ${valorjuros} em 4 parcelas de ${valorjuros/4:.2f}')
    elif parcelas == 5:
        print(f'O seu total é ${valorjuros} em 5 parcelas de ${valorjuros/5:.2f}')
    elif parcelas == 6:
        print(f'O seu total é ${valorjuros} em 6 parcelas de ${valorjuros/6:.2f}')
    else:
        print(f'{parcelas} não é um numero valido de parcelas! Repita o processo')

else:
    print(f'{formadepgto} não é uma entrada valida. Repita o processo')
