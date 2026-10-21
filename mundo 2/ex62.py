valorinicial = int(input('Digite o valor inicial:   '))
razao = int(input('Digite a razão da sua PA:   '))
qt = int(input('Quantos termos você deseja saber:   '))
original = qt
opcao = 1
while opcao != 0:
    if original != 1:
        print(f'{valorinicial}', end = ' -> ')
    else:
        print(f'{valorinicial}')
        opcao = int(input('Quantos termos além você deseja saber:  '))
        original += opcao
        if opcao != 0:
            continue
    valorinicial += razao
    original -= 1
print('Programa encerrado')