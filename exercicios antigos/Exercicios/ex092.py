from datetime import date

year = date.today().year

trabalhador = dict()
trabalhador['Nome'] = str(input('Digite o nome: ')).strip().title()
nascimento = int(input('Digite o ano de nascimento: '))
trabalhador['Idade'] = year - nascimento
trabalhador['CTPS'] = int(input('Digite o numero da Carteira de trabalho(0 se desempregado): '))

if trabalhador['CTPS'] != 0:

    trabalhador['Ano de contratação'] = int(input('Digite o ano de contratação: '))
    trabalhador['Salario'] = float(input('Digite o salario: R$'))

    aposentadoria = (35 - (year - trabalhador['Ano de contratação'])) + trabalhador['Idade']

    trabalhador['Aposentadoria'] = aposentadoria

for k, v in trabalhador.items():

    print(f'{k} = {v}')
