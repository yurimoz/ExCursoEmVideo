from fileinput import close
from os import write

from modulos import cores
from time import sleep

from modulos.cores import ciano


def arquivoexiste(nome):

    try:
        arq = open(nome, 'rt')
        arq.close()

    except (FileNotFoundError, FileNotFoundError):

        return False

    else:

        return True


def criaarquivo(nome):

    try:
        a = open(nome, 'wt+')
        a.close()

    except:
        print(cores.vermelho('Houve um erro na criação do arquivo!'))
        return False

    else:
        print(cores.verde(f'Arquivo {nome} criado com sucesso'))
        return True

def lerarquivo(nome):

    try:
        a = open(nome, 'rt')

    except:

        print(cores.vermelho('TIVEMOS PROBLEMAS AO LER O ARQUIVO'))

    else:

        for linha in a:

            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(ciano(f'{dado[0]:.<20}{dado[1]:.>10} anos'))

    finally:

        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):

    try:
        arquivo = open(arq, 'at')

    except:
        print('Houve um erro ao tentar abrir o arquivo')

    else:
        try:
            arquivo.write(f'{nome};{idade}\n')

        except:

            print('Houve um erro ao escrever os dados')

        else:
            print(f'{nome} cadastrado com sucesso!')

    finally:
        arquivo.close()