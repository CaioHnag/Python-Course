lista = list()
par = list()
impar = list()
op = 'S'
while op != 'N':
    user = int(input('Digite o número:  '))
    lista.append(user)
    if user % 2 == 0 :
        par.append(user)
    else:
        impar.append(user)
    op = input('Deseja continuar? [S/N] ').strip().upper()[0]
    while op not in ['S' , 'N']:
        op = input('Deseja continuar? [S/N] ').strip().upper()[0]
print(f'Lista original = {lista}')
print(f'Lista par = {par}')
print(f'Lista impar = {impar}')