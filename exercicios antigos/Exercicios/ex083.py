aberto = 0
fechado = 0
errado = False

exp = str(input('Digite uma expressão matematica: '))

if exp.count('(') != exp.count(')'):

    errado = True

else:

    for i in exp:

        if i == '(':

            aberto += 1

        if i == ')':

            fechado += 1

        if fechado > aberto:

            errado = True
            break

if errado is True:

    print('A expressão digitada é invalida')

else:
    print('A expressão digitada esta correta')

