from datetime import date

ano = date.today().year
nascimento = int(input('Em que ano você nasceu? '))
idade = ano - nascimento

if idade > 18:
    print(f'Ja passou da hora de você se alistar!! Você deveria ter se alistado em {ano - (idade - 18)}')

elif idade < 18:
    print(f'Ainda não está na hora de você se alistar. Seu alistamento será em {ano + (18 - idade)}')

else:
    print('Você deve se alistar esse ano!!')
