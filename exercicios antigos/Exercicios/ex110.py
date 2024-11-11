from modulos.moeda import moeda

p = float(input('Digite o preço: '))
pa = float(input('Digite a porcentagem de aumento: '))
pd = float(input('Digite a porcentagem de redução: '))

moeda.resumo(p, pa, pd)