def area(larg , comprimento):
    ar = larg * comprimento
    print(f'A area do terreno {larg}x{comprimento} é igual a {ar:.2f}m2')
a = float(input('Largura: '))
b = float(input('Comprimento: '))
area(a,b)
