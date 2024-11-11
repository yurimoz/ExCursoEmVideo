from modulos.moeda import moeda


p = float(input('Digite o preço: '))
pa = float(input('Digite a porcentagem que vai aumentar: '))
pd = float(input('Digite a porcentagem que vai diminuir: '))

print(f'Dobro de {p} é {moeda.dobro(p, form=False)}')
print(f'Metade de {p} é {moeda.metade(p, form=False)}')
print(f'Aumentando {pa}% da {moeda.aumentar(p, pa)}')
print(f'Diminuindo {pd}% da {moeda.diminuir(p, pd)}')