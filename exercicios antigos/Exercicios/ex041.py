from datetime import date

ano = date.today().year
nascimento = int(input('Em que ano você nasceu? '))
idade = ano - nascimento
categoria = 'MIRIM'

if idade > 20:
    categoria = 'MASTER'

elif idade > 19:
    categoria = 'SENIOR'

elif idade > 14:
    categoria = 'JUNIOR'

elif idade > 9:
    categoria = 'INFANTIL'

print(f'Idade em {ano}: {idade}')
print(f'Categoria: {categoria}')
