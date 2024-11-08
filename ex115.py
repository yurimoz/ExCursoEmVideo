import os
from menu115 import criamenu
import arquivo
from modulos import linhas
from modulos.dados import numeros


os.system('')

arq = 'listanome.txt'

existe = arquivo.arquivoexiste(arq)

if existe is False:

    existe = arquivo.criaarquivo(arq)

if existe:

    while True:

        resp = criamenu('Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema')

        if resp == 1:

            linhas.linhamenu('Pessoas Cadastradas!', '~')
            arquivo.lerarquivo(arq)

            voltar = criamenu('Sim', 'Não', msg='Deseja Voltar?')

            if voltar == 1:
                continue

            elif voltar == 2:
                resp = 3

        if resp == 2:

            linhas.linhamenu('Cadastro de pessoas!', '~')
            nome = str(input('Nome: ')).strip().title()
            idade = numeros.leiaInt('Idade: ')

            arquivo.cadastrar(arq, nome, idade)

            voltar = criamenu('Sim', 'Não', msg='Deseja Voltar?')

            if voltar == 1:
                continue

            elif voltar == 2:
                resp = 3

        if resp == 3:
            print('Saindo do sistema...')
            break



