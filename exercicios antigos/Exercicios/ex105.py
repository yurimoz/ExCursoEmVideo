def notas(*nots, sit=False):
    '''
    --> A função notas serve para armazenar e a analisar as notas de varios alunos
    :param nots: notas dos alunos
    :param sit: True para retornar a situação de cada aluno, False por padrão não retorna a situação
    :return: Retorna um dicionario com o total de notas da turma, a menor e maior nota, a media da turma, e opcionalmente
    a situação de cada aluno
    '''
    turma = dict()
    maior = nots[0]
    menor = nots[0]
    turma['total'] = len(nots)

    for nota in nots:
        if nota > maior:
            maior = nota

        if nota < menor:
            menor = nota

    turma['maior'] = maior
    turma['menor'] = menor

    turma['media'] = sum(nots) / len(nots)

    aluno = list()

    if sit:
        for i in range(0, len(nots)):
            if nots[i] >= 7:
                situ = 'APROVADO'
            elif nots[i] >= 5:
                situ = 'RECUPERAÇÃO'
            else:
                situ = 'REPROVADO'

            aluno.append(nots[i])
            aluno.append(situ)

            turma[f'aluno{i}'] = aluno.copy()

            aluno.clear()


    return turma


turminha = notas(5, 10, 10, 2, sit=True)
turmicha = notas(2, sit=True)
turmona = notas(3.5, 8.2, 7, 10, 9, 2, 6.8, sit=True)
turmera = notas(1, 2, 5, 7)
print(turminha)
print(turmicha)
print(turmona)
print(turmera)
help(notas)
