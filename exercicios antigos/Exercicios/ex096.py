def area(largura, comprimento):
    a = largura * comprimento
    print(f'Um terreno com {largura}m de largura e {comprimento}m de comprimento tem uma area de {a:.2f}m²')
    return largura * comprimento

area(float(input('Digite a largura: ')), float(input('Digite o comprimento: ')))
