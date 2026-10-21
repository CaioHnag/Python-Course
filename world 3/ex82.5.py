lista = list()
par = list()
impar = list()
op = 'S'
while op != 'N' :
    user = int(input('Digite um número:  '))
    lista.append(user)
    op = input('Deseja continuar? [S/N] ').strip().upper()[0]
    while op not in ['S' , 'N'] :
        op = input('Deseja continuar? [S/N] ').strip().upper()[0]
for valor in lista :
    if valor % 2 == 0:
        par.append( valor )
    else:
        impar.append( valor)
print(f'Lista original = { lista }')
print(f'Pares = {par}')
print(f'Impares = {impar}')