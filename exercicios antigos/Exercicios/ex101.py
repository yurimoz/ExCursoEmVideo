from datetime import datetime


def voto(ano):
    idade = datetime.now().year - ano

    if 65 > idade >= 18:
        return f'{idade} anos. VOTO OBRIGATORIO!'

    elif idade >= 16:
        return f'{idade} anos. VOTO OPCIONAL'

    else:
        return f'{idade} anos. VOTO NEGADO!'


nascimento = int(input('Digite o ano de nascimento: '))
situacao = voto(nascimento)
print(situacao)