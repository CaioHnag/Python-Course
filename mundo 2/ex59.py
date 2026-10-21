n1 = 0
n2 = 0
while True:
    print('[1] == Somar\n[2] == Multiplicar\n[3] == Maior\n[4] == Novos números\n[5] == sair')
    usuario = int(input('Oque você deseja fazer:   '))
    if usuario == 5:
        break
    n1 = int(input('Número:  '))
    n2 = int(input('Número:  '))
    if usuario == 1:
        print(f'{n1} + {n2} = {n1 + n2}')
    elif usuario == 2:
        print(f'{n1} x {n2} = {n1 * n2}')
    elif usuario == 3:
        print(f'O maior número é: {max(n1,n2)}')
    elif usuario == 4:
        print('Digite os novos números.')
        n1 = int(input('Número:  '))
        n2 = int(input('Número:  '))
    else:
        print('Opção invalida, digite novamente.')
        usuario = int(input('Digite aqui:  '))
print('Você encerrou sua sessão.')
