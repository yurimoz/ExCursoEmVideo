import os
from modulos import cores
import urllib.request

os.system('')

try:
    site = urllib.request.urlopen(f'https://{input("Digite o site:")}')

except:
    print(cores.vermelho('O SITE NÃO ESTÁ ACESSIVEL'))

else:
    print(cores.verde('O site está funcionando corretamente'))