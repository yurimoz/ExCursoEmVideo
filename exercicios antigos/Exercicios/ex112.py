from modulos.dado import dado
from modulos.moeda import moeda

p = dado.leiaDinheiro('Digite o preço: R$')
pa = float(input('Digite a porcentagem de aumento: '))
pd = float(input('Digite a porcentagem de redução: '))

moeda.resumo(p, pa, pd)
