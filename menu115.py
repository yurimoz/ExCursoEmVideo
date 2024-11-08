from modulos import linhas
from modulos import cores
from modulos.dados import entrada



def criamenu(*opcoes, msg='MENU PRINCIPAL'):

   while True:

      linhas.linhamenu(msg)

      for i, o in enumerate(opcoes):

         print(cores.roxo(f'{i + 1} -- {cores.azul(o)}'))


      linhas.crialinha(50)

      n = entrada.entradaint(cores.roxo('Sua Opção: '), limsup=len(opcoes))


      return n

