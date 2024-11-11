def escreva(txt):
    txt = str(txt).strip()
    print('~'*(len(txt) + 10))
    print(txt.center((len(txt) + 10)))
    print('~'*(len(txt) + 10))


escreva(str(input('Digite um texto: ')))