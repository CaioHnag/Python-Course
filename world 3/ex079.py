lista = []
op = 'S'
while op == 'S':
    a = int(input('Digite um valor: '))
    if a not in lista:
        print('Valor adicionado com sucesso...')
        lista.append(a)
    else:
        print('Valor já existente na lista , não vou adicionar - lo')
    op = input('Deseja continuar? [S/N] ').strip().upper()[0]
    while op not in ['S', 'N']:
        op = input('Deseja continuar? [S/N] ').strip().upper()[0]
lista.sort()
print(f'Valores adicionados = { lista } ')