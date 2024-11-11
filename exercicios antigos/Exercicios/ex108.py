from modulos.moeda import moeda

p = float(input('Digite o preço: R$'))
pa = float(input('Digite a porçentagem pela qual deseja aumentar: '))
pd = float(input('Digite a porcentagem pela qual deseja diminuir: '))

print(f'O dobro de R${p:.2f} é {moeda.dobro(p)}')
print(f'A metade de R${p:.2f} é {moeda.metade(p)}')
print(f'Aumentando R${p:.2f} em {pa}% temos {moeda.aumentar(p, pa)}')
print(f'Diminuindo R${p:.2f} em {pd}% temos {moeda.diminuir(p, pd)}')