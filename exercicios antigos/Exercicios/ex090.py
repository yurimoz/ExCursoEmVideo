aluno = {}
aluno['nome'] = str(input('Digite o nome do aluno: ')).strip().title()
aluno['media'] = float(input(f'Digite a media de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'APROVADO'

elif aluno['media'] >= 5:
    aluno['situação'] = 'RECUPERAÇÃO'

else:
    aluno['situação'] = 'REPROVADO'

for k,v in aluno.items():
    print(f'{k} = {v}')